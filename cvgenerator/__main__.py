import argparse
import logging
import cvgenerator.app as app
import os.path as path
import os
import sys

CWD = os.getcwd()
DIRECTORIES = [ 'education', 'work_experience' ]

def main():
    '''Attempts to parse the input file path and upload it to a sqlite3 database.'''
    parser = argparse.ArgumentParser(description='Utility to help create CV information without constantly having to rewrite information.')
    parser.add_argument('--initialise', '-init', help='Creates cv_bin directory to store your CV information if it does not already exist', action='store_true')
    parser.add_argument('--edit_your_cv', '-e', help='Menu to edit your CV information.', action='store_true')
    parser.add_argument('--log_verbosity', '-v', type=int, default=2, help='Logging verbosity (1 to 5) - level 1 is most verbose, level 5 logs critical entries only.')
    args = parser.parse_args()
    root_directory = 'cv_bin'

    if args.initialise == True:
        if not path.exists(root_directory):
            os.mkdir(root_directory)
            for directory in DIRECTORIES:
                if not path.exists(path.join(root_directory, directory)):
                    os.mkdir(path.join(root_directory, directory))
    else:
        if not path.exists(root_directory):
            print('If your CV data already exists, please navigate to its root directory, otherwise run \'cvgenerator -init\' to get started.')
            sys.exit(1)

    os.chdir(root_directory)
    app.run()

if __name__ == "__main__":
    main()