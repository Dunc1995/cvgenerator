import argparse
import logging
import cvgenerator as cv
import os.path as path
import os
import sys
from tinydb import TinyDB, Query
import cvgenerator.wrappers.tinydb as db

def main():
    '''Attempts to parse the input file path and upload it to a sqlite3 database.'''
    parser = argparse.ArgumentParser(description='Utility to help create CV information without constantly having to rewrite information.')
    parser.add_argument('--initialise', '-init', help='Creates cv_bin directory to store your CV information if it does not already exist', action='store_true')
    parser.add_argument('--log_verbosity', '-v', type=int, default=2, help='Logging verbosity (1 to 5) - level 1 is most verbose, level 5 logs critical entries only.')
    args = parser.parse_args()

    if args.initialise == True:
        if not path.exists(cv.ROOT_DIRECTORY):
            os.mkdir(cv.ROOT_DIRECTORY)
    else:
        if not path.exists(cv.ROOT_DIRECTORY):
            print('If your CV data already exists, please navigate to its root directory, otherwise run \'cvgenerator -init\' to get started.')
            sys.exit(1)

    os.chdir(cv.ROOT_DIRECTORY)
    cv.DB_CLIENT = db.client()
    cv.MAIN_MENU.show()

if __name__ == "__main__":
    main()