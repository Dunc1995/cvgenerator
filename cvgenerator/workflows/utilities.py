import cvgenerator.forms as forms
import cvgenerator as cv
from cvgenerator.wrappers.pyinquirer import prompts
import json
import cvgenerator.parser as parser
import cvgenerator.navigator as navigator
import textwrap

def show_help():
    text = '''
    --- Summary ---
    Schemas exist to enforce your document's structure. The schemas_hierarchy.yaml in your
    ./cv_bin/config directory defines your document's schema types. The cvgenerator application
    parses this .yaml file to create JSON objects that define metadata for every piece of 
    information you add to your document.
    --- Commands ---
    1. \"Edit default schema names\" allows you to set default names for all of your schemas.
    For example a \'work_experience_section\' will always be called \"Work Experience\".
    2. \"Edit default schema tags\"  allows you to assign default tags to all of your document's
    schemas. For example a Summary section may be optional whereas a Work Experience section is
    mandatory.
    3. \"Refresh schema hierarchy\" will reload the schema_hierarchy.yaml config file and
    repopulate the schemas table in db.json. IT IS WORTH NOTING that this may remove any
    tags that have been previously added to your data schemas; this should only be used if
    you're planning on defining a new document structure.
    '''
    #TODO find a better way to print
    print(text)

def edit_default_schema_tags():
    navigator.start()

def edit_default_schema_names():
    # tags_array = cv.DB_CLIENT.get_all_tags()
    # prompts.checkbox(tags_array)
    print('Not Implemented')

def edit_schema_hierarchy():
    prompts.edit_existing_file(cv.SCHEMAS_PATH)
    refresh_schema_hierarchy(message='Do you want your changes to be reflected now?\n This will delete any default tags you have assigned to your data.')

def edit_tag_options():
    prompts.edit_existing_file(cv.TAGS_PATH)
    refresh_tag_options()

def refresh_schema_hierarchy(message='This will delete any default tags you have added to your data.\n Are you sure you want to continue?'):
    should_continue = prompts.confirm(message)

    if should_continue == True:
        schemas_list = parser.get_schemas_from_yaml()
        cv.DB_CLIENT.drop_table('schemas')
        for schema in schemas_list:
            cv.DB_CLIENT.insert_schema_entry(schema)

def refresh_tag_options():
    tags_dict = parser.get_tags_from_yaml()
    cv.DB_CLIENT.drop_table('tags')
    cv.DB_CLIENT.insert_tags(tags_dict)
