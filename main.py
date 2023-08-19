from word.engine import wordengine
from base.engine import base



# loop download and writing new information in base
def main_loop():
    while True:

        # looking for parcers
        sites_for_parcing = []
        sites = loadparcers()
        
        # Parce information from parcers
        for site in sites:
            #fetch txt from site
            # process txt to words list
            wordlist = wordengine(site.txt())
            #wordlist = 
            base.insert(wordlist, site.name())




        



if __name__ == "__main__":
    main_loop()