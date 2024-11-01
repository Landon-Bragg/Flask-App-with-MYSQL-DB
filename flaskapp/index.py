from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jbnv;jksndfo'
bootstrap = Bootstrap(app)


class LoginForm(FlaskForm):
    email = StringField('Email address', validators=[DataRequired()])
    submit = SubmitField('Log in')

@app.route('/')
def about():
    return render_template("about.html")


@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('login', email=form.email.data))
    return render_template('index.html', form=form)

@app.route('/login/<email>', methods=['GET'])
def login(email):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM customer WHERE email = %s", (email,))
    customer = cursor.fetchone()
    cursor.close()

    if customer:
        session['customer_id'] = customer[0]
        session['customer_name'] = f"{customer[1]} {customer[2]}"
        flash(f"Welcome, {session['customer_name'][1:]}!", 'success')
        return redirect(url_for('home'))
    else:
        flash('Invalid email address.', 'danger')
        return redirect(url_for('index'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/browse_db')
def browse_db():
    cursor = db.cursor()
    cursor.execute("show tables")
    tables = [field[0] for field in cursor.fetchall()[1:]]
    cursor.close()
    return render_template('browse_db.html', dbname=dbname, tables=tables)


from datetime import datetime

@app.route('/table/<table>', methods=['GET'])
def table(table):
    cursor = db.cursor()
    sort_by = request.args.get('sort_by', None)
    order = request.args.get('order', 'asc')

    if sort_by:
        sort_order = 'ASC' if order == 'asc' else 'DESC'
        
        # Check if the sort_by column is a date or datetime column
        cursor.execute(f"SHOW COLUMNS FROM {table} WHERE Field = '{sort_by}'")
        column_type = cursor.fetchone()[1]
        if 'date' in column_type.lower() or 'time' in column_type.lower():
            query = f"SELECT * FROM {table} ORDER BY STR_TO_DATE({sort_by}, '%Y-%m-%d %H:%i:%s') {sort_order}"
        else:
            query = f"SELECT * FROM {table} ORDER BY {sort_by} {sort_order}"
    else:
        query = f"SELECT * FROM {table}"

    cursor.execute(query)
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    cursor.close()
    return render_template('table.html', table=table, columns=column_names, rows=rows, sort_by=sort_by, order=order)

@app.route('/user_info', methods=['GET'])
def user_info():
    if 'customer_id' not in session:
        flash('You must be logged in to access this page.', 'warning')
        return redirect(url_for('index'))

    cursor = db.cursor()
    cursor.execute("SELECT * FROM customer WHERE customer_id = %s", (session['customer_id'],))
    customer = cursor.fetchone()
    cursor.close()

    if customer:
        return render_template('user_info.html', customer=customer)
    else:
        flash('An error occurred while fetching user information.', 'danger')
        return redirect(url_for('index'))
    


if __name__ == '__main__':
    dbname = 'sakila'
    db = pymysql.connect(host='localhost',
                         user='root', passwd='Landon123', db=dbname)
    app.run(debug=True)
    db.close()
