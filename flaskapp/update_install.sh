source venv/bin/activate

python3 -m pip install --upgrade pip
pip3 install --upgrade pip

pip3 freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip3 install -U

pip3 install -r requirements.txt