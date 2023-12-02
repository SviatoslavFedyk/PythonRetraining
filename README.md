#Create venv
python -m venv .venv

#Activate venv 
source .venv/bin/activate

#Upgrade requirements
pip freeze > requirements.txt

#Install all needed packages
pip install -r requirements.txt
