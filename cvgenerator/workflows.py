from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import prompt
import json
import cvgenerator as cv
from tinydb import Query
import cvgenerator.forms as forms

__SCHEMA_PLACEHOLDER = None

def placeholder():
    print('Route not yet implemented...')

def view_data_types():
    placeholder()

def upsert_list(db_obj, list_name : str):
    query = Query()
    list_obj = __get_entries_list(db_obj, list_name)
    list_name_singular = list_name[:-1]

    questions = {
        'type': 'input',
        'name': list_name_singular,
        'message': 'Enter a new {} name.'.format(list_name_singular),
    }
    answers = prompt(questions)
    list_obj.append(answers[list_name_singular])

    db_obj.upsert({'name': list_name, 'entries': list_obj}, query.name == list_name)

def __get_entries_list(db_obj, list_name):
    query = Query()
    list_obj = None
    try:
        list_obj = db_obj.search(query.name == list_name)[0]['entries']
    except IndexError as e:
        list_obj = []
    return list_obj

def insert_tag():
    upsert_list(cv.TAGS, 'tags')

def insert_data_type():
    upsert_list(cv.TYPES, 'types')

def insert_data():
    #TODO query existing data types and print here
    data_types = __get_entries_list(cv.TYPES, 'types')

    questions = [ {
        'type': 'list',
        'name': 'type',
        'message': 'What type of data is this data?',
        'choices': data_types
    },
    {
        'type': 'input',
        'name': 'name',
        'message': 'Enter a name for this new entry.',
    } ]
    answers = prompt(questions)
    cv.DATA.insert({ 
        'type': answers['type'],
        'name': answers['name'],
        'contents': {},
        'tags': [] })

def assign_tags_to_data():
    print(cv.DATA.all())
    placeholder()

def edit_type_schemas():
    global __SCHEMA_PLACEHOLDER
    query = Query()
    schema_to_edit = None
    data_types = __get_entries_list(cv.TYPES, 'types')
    questions = {
        'type': 'list',
        'name': 'type',
        'message': 'Select a data type to edit.',
        'choices': data_types
    }
    answers = prompt(questions)
    schema_to_edit = __get_schema(answers['type'])

    print('The following schema exists for the {} type:\n'.format(answers['type']))
    print(json.dumps(schema_to_edit, indent=4))

    __SCHEMA_PLACEHOLDER = schema_to_edit
    cv.SCHEMA_MENU.show()

def add_schema_key():
    global __SCHEMA_PLACEHOLDER
    query = Query()
    new_key = forms.input_prompt('key', 'Please enter a key name')
    __SCHEMA_PLACEHOLDER[new_key] = None
    cv.SCHEMAS.upsert(__SCHEMA_PLACEHOLDER, query.type == __SCHEMA_PLACEHOLDER['type'])

def remove_schema_key():
    global __SCHEMA_PLACEHOLDER
    query = Query()
    questions = {
        'type': 'list',
        'name': 'key',
        'message': 'Please select a key to remove.',
        'choices': __SCHEMA_PLACEHOLDER.keys()
    }
    answer = prompt(questions)
    
    #__SCHEMA_PLACEHOLDER[answer['key']] = None
    #cv.SCHEMAS.upsert(__SCHEMA_PLACEHOLDER, query.type == __SCHEMA_PLACEHOLDER['type'])

def add_type_parent():
    placeholder()

def remove_type_parent():
    placeholder()

def __get_schema(type_name: str):
    schema = None
    query = Query()
    try:
        schema = cv.SCHEMAS.search(query.type == type_name)[0]
    except IndexError as e:
        schema = cv.DEFAULT_SCHEMA
        schema['type'] = type_name
        cv.SCHEMAS.upsert(schema, query.type == type_name)
    return schema

def __upsert(table, dict_input, name, key = 'name'):
        table.upsert(dict_input, Query()[key] == name)