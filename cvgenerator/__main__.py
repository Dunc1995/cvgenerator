import argparse
import logging
import cvgenerator as cv
import os.path as path
import os
import sys
import cvgenerator.forms as forms
import cvgenerator.wrappers.tinydb as db
import cvgenerator.parser as resource_parser

def main():
    '''Attempts to parse the input file path and upload it to a sqlite3 database.'''
    parser = argparse.ArgumentParser(description='Utility to help create CV information without constantly having to rewrite information.')
    parser.add_argument('--initialise', '-init', help='Creates cv_bin directory to store your CV information if it does not already exist', action='store_true')
    parser.add_argument('--log_verbosity', '-v', type=int, default=2, help='Logging verbosity (1 to 5) - level 1 is most verbose, level 5 logs critical entries only.')
    args = parser.parse_args()

    if args.initialise == True:
        schema_template = resource_parser.get_schema_template()

        if not path.exists(cv.ROOT_DIRECTORY):
            os.mkdir(cv.ROOT_DIRECTORY)
            schema_path = os.path.join(cv.ROOT_DIRECTORY, 'schemas_hierarchy.yaml')
            write_to_file(schema_path, schema_template)
    else:
        if not path.exists(cv.ROOT_DIRECTORY):
            print('If your CV data already exists, please navigate to its root directory, otherwise run \'cvgenerator -init\' to get started.')
            sys.exit(1)

    os.chdir(cv.ROOT_DIRECTORY)
    cv.DB_CLIENT = db.client()
    forms.MAIN_MENU.show()

def write_to_file(file_path: str, contents: str):
    with open(file_path, 'w') as file:
        file.write(contents)
        file.close()

if __name__ == "__main__":
    main()