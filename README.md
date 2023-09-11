<br />
  <h1 align="center">Linguistic Analysis using NLP</h1> 
  <h3 align="center">
  Author: Aleksander Moeslund Wael <br>
  </h3>
</p>

## About the project
This repo contains a Python script called ``get_linguistic_features.py`` - an information extraction script which performs part-of-speech (PoS) tagging and named-entity recognition (NER). It extracts the relative frequency of Nouns, Verbs, Adjective, and Adverbs per 10,000 words and the total number of *unique* persons (PER), locations (LOC), and organisations (ORGS). The extracted information is then saved for analysis or other use.

### Data
For this project, the Uppsala Student English Corpus (USE) was used. Documentation can be found [here](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457). The following information can be found in the documentation: "The corpus consists of 1,489 essays written by 440 Swedish university students of English at three different levels, the majority in their first term of full-time studies. The total number of words is 1,221,265, which means an average essay length of 820 words. A typical first-term essay is somewhat shorter, averaging 777 words." The essays are stored across 14 sub-folders in the `USEcorpus` folder. The sub-folders correspond to term, style and subject of the essays.

### Model
The information extraction is done using the `en_core_web_md` SpaCy model for Python. It is a medium-size pretrained model suited for a variety of english NLP tasks.

### Pipeline
The ``get_linguistic_features.py`` follows these steps:
1. Import dependencies
2. Load SpaCy model
3. Initialize information extraction per sub-folder
4. Append information to a `pandas` dataframe and save it as a .csv file in the `out` folder

## Requirements

The code is tested on Python 3.11.2. Futhermore, if your OS is not UNIX-based, a bash-compatible terminal is required for running shell scripts (such as Git for Windows).

## Usage

The repo was setup to work with Windows (the WIN_ files), MacOS and Linux (the MACL_ files).

### 1. Clone repository to desired directory

```bash
git clone https://github.com/alekswael/PoS_NER_tagger
cd PoS_NER_tagger
```
### 2. Run setup script 
**NOTE:** Depending on your OS, run either `WIN_setup.sh` or `MACL_setup.sh`.

The setup script does the following:
1. Creates a virtual environment for the project
2. Activates the virtual environment
3. Installs the correct versions of the packages required
5. Deactivates the virtual environment

```bash
bash WIN_setup.sh
```

### 3. Run pipeline
**NOTE:** Depending on your OS, run either `WIN_run.sh` or `MACL_run.sh`.

Run the script in a bash terminal.

The script does the following:
1. Activates the virtual environment
2. Runs `get_linguistic_features.py` located in the `src` folder
3. Deactivates the virtual environment

```bash
bash WIN_run.sh
```

## Note on model tweaks
Some model parameters can be set through the ``argparse`` module. However, this requires running the Python script seperately OR altering the `run*.sh` file to include the arguments. The Python script is located in the `src` folder. Make sure to activate the environment before running the Python script.

```
get_linguistic_features.py [-h] [--folder FOLDER]

options:
  -h, --help       show this help message and exit
  --folder FOLDER  Relative path to the corpus folder (default: USEcorpus)
```

## Repository structure
This repository has the following structure:
```
│   .gitignore
│   MACL_run.sh
│   MACL_setup.sh
│   README.md
│   requirements.txt
│   WIN_run.sh
│   WIN_setup.sh
│
├───.github
│       .keep
│
├───in
│   └───USEcorpus
│       ├───a1
│       │       0100.a1.txt
│       │       ...
│       ├───a2
│       │       0100.a2.txt
│       │       ...
│       ...
│       └───c1
│               0140.c1.txt
│               ...
│
├───out
│       .gitkeep
│
└───src
        .gitkeep
        get_linguistic_features.py
```

## Example of saved table

```
Folder: a1

    Text_name     RF_NOUN   RF_VERB   RF_ADJ   RF_ADV    U_PER  U_LOC  U_ORG
0   0100.a1.txt   1530.9    1221.91   800.56   533.71    0      0      0
1   0101.a1.txt	  1165.41   1240.6    588.97   839.6     0      0      0
2   0102.a1.txt	  1493.98   1204.82	  686.75   481.93    0      0      0
3   0103.a1.txt   1096.35   1362.13	  598.01   575.86    0      0      3
4   0104.a1.txt   1320.99   1197.53	  567.9    679.01    0      1      5
```

