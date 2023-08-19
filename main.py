from word.engine import wordengine



# loop download and writing new information in base
def main_loop():
    while True:

        # looking for parcers
        sites_for_parcing = []
        sites = loadparcers()
        
        # Parce information from parcers
        for parcer in parcers:
            txt = parcer.txt()

        



if __name__ == "__main__":
    main_loop()