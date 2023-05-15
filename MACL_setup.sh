# Create a virtual environment
python3 -m venv linguistics_venv

# Activate the virtual environment
source ./linguistics_venv/bin/activate

# Install requirements
python3 -m pip install --upgrade pip
python3 -m pip install -r ./requirements.txt
python3 -m spacy download en_core_web_md

# deactivate
deactivate

#rm -rf linguistics_venv