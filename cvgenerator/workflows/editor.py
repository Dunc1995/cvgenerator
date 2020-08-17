from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import prompt
import json
import cvgenerator as cv
from tinydb import Query
import cvgenerator.forms as forms

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