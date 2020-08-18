import cvgenerator.forms as forms
from cvgenerator import DB_CLIENT as db
from cvgenerator.wrappers.pyinquirer import prompts

def insert_data():
    #TODO query existing data types and print here
    pass
    # data_types = __get_entries_list(cv.TYPES, 'types')

    # questions = [ {
    #     'type': 'list',
    #     'name': 'type',
    #     'message': 'What type of data is this data?',
    #     'choices': data_types
    # },
    # {
    #     'type': 'input',
    #     'name': 'name',
    #     'message': 'Enter a name for this new entry.',
    # } ]
    # answers = prompt(questions)
    # cv.DATA.insert({ 
    #     'type': answers['type'],
    #     'name': answers['name'],
    #     'contents': {},
    #     'tags': [] })

def assign_tags_to_data():
    pass
    # print(cv.DATA.all())
    # placeholder()