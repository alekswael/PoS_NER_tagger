# Create a virtual environment
python -m venv linguistics_venv

# Activate the virtual environment
source ./linguistics_venv/Scripts/activate

# Install requirements
python -m pip install --upgrade pip
python -m pip install -r ./requirements.txt
python -m spacy download en_core_web_md

# deactivate
deactivate

#rm -rf linguistics_venv