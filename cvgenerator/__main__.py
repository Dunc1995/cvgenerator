import argparse
import logging
import cvgenerator.app as app
import os

def main():
    '''Attempts to parse the input file path and upload it to a sqlite3 database.'''
    parser = argparse.ArgumentParser(description='Utility to help create CV information with constantly having to rewrite information.')
    parser.add_argument('--initialise_data_folder', '-init', type=str, help='Creates bin directory to store your CV information')
    parser.add_argument('--log_verbosity', '-v', type=int, default=2, help='Logging verbosity (1 to 5) - level 1 is most verbose, level 5 logs critical entries only.')
    args = parser.parse_args()
    print(os.getcwd())
    app.run()

if __name__ == "__main__":
    main()