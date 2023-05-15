# Importing packages needed for the assignment.
import argparse # Package for parsing command line arguments.
import os # For navigating the file system.
import spacy # For NLP.
import pandas as pd # For data manipulation.
import warnings # For ignoring warnings.
warnings.filterwarnings("ignore") # Ignore warnings.

def input_parse(): # Function to parse command line arguments.
    # initialize the parser
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # add arguments
    parser.add_argument("--folder",
                        help="Relative path to the corpus folder",
                        default="USEcorpus",
                        type=str)
    # parse the arguments from the command line
    args = parser.parse_args()
    # get the name
    return args


# First thing to do is to load the spacy model. Only need to do this once.
nlp = spacy.load("en_core_web_md")

def get_linguistic_features(folder):
    # I set a single path to the folder with the corpus.
    path_to_folder = os.path.join(os.getcwd(), "in", folder)
    
    # Since there are 14 subfolders, I need to loop over them. I use os.listdir to get a list of the subfolders.
    subfolders = os.listdir(path_to_folder)
    
    # THIS IS THE COMPLETE LOOP WHICH RETURNS A .CSV FILE FOR EACH SUBFOLDER
    # There are 3 loops nested in total. The first loop is over the subfolders.
    for x in subfolders:
        
        # I join the folder path with the subfolder name to get the full path to the subfolder.
        folder = os.path.join(path_to_folder, x)
        
        # I create an empty dataframe here, because I want a dataframe for each subfolder.
        df = pd.DataFrame(columns=["text_name", "RelFreq_NOUN", "RelFreq_VERB", "RelFreq_ADJ", "RelFreq_ADV", "Unique_PER", "Unique_LOC", "Unique_ORG"])

        # The second loop is over the files in the subfolder.
        for y in os.listdir(folder): 
            
            # Defining the full path to the file
            file_path = os.path.join(folder, y) # NEED FULL PATH
            
            # Reading the file
            f = open(file_path, "r", encoding="ISO-8859-1")
            file = f.read()
            
            # I now create a spacy object by passing the text to the NLP object.
            file_text = nlp(file)
            
            # Here is where I create lists for the POS and NER tags.
            # The non_words_counter is used to remove punctutation, spaces, symbols and other non-words from the relative frequency calculations.
            non_words_counter = 0
            nouns = []
            verbs = []
            adjectives = []
            adverbs = []
            PER = []
            LOC = []
            ORG = []

            # The third loop is over the tokens in the text.
            for token in file_text:
                
                # Here, I use a series of if statements to check for the POS and NER tags and append them to the appropriate list.
                # I use if and not elif statements, because tokens can have both a POS and a NER tag.
                if token.pos_ == "X" or token.pos == "PUNCT" or token.pos == "SPACE" or token.pos == "SYM":
                    non_words_counter += 1
                if token.pos_ == "NOUN":
                    nouns.append(token.text)
                if token.pos_ == "VERB":
                    verbs.append(token.text)
                if token.pos_ == "ADJ":
                    adjectives.append(token.text)
                if token.pos_ == "ADV":
                    adverbs.append(token.text)
                if token.ent_type_ == "PER":
                    PER.append(token.text)
                if token.ent_type_ == "LOC":
                    LOC.append(token.text)
                if token.ent_type_ == "ORG":
                    ORG.append(token.text)
            
            # Here, I calculate the relative frequencies and the amount of unique entities. I round the relative frequencies to 2 decimals.
            RelFreq_NOUN = round(len(nouns) / (len(file_text) - non_words_counter) * 10000, 2)
            RelFreq_VERB = round(len(verbs) / (len(file_text) - non_words_counter) * 10000, 2)
            RelFreq_ADJ = round(len(adjectives) / (len(file_text) - non_words_counter) * 10000, 2)
            RelFreq_ADV = round(len(adverbs) / (len(file_text) - non_words_counter) * 10000, 2)
            Unique_PER = len(set(PER))
            Unique_LOC = len(set(LOC))
            Unique_ORG = len(set(ORG))
            
            # I then append the results to the dataframe, so each row in the df is a text file.
            df = df.append({"text_name": y, "RelFreq_NOUN": RelFreq_NOUN, "RelFreq_VERB": RelFreq_VERB, "RelFreq_ADJ": RelFreq_ADJ, "RelFreq_ADV": RelFreq_ADV, "Unique_PER": Unique_PER, "Unique_LOC": Unique_LOC, "Unique_ORG": Unique_ORG}, ignore_index=True)
        
        # Lastly, as part of the first loop, I save the dataframe as a .csv file in the out folder. It gets named after the subfolder.
        df.to_csv(os.path.join(os.getcwd(), "out", x + ".csv"))
        
        # The result is a .csv file for each subfolder in the corpus located in the "out" folder.
        # Message to display in the terminal when the script is done.
        print("Done with " + x + "!")
        
    print("DONE WITH ALL SUBFOLDERS!")

# Define main function

def main():
    args = input_parse()
    # pass name to hello function
    get_linguistic_features(args.folder)

if __name__ == "__main__":
    main()