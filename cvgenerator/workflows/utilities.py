import cvgenerator.forms as forms
from cvgenerator import DB_CLIENT as db
from cvgenerator.wrappers.pyinquirer import prompts

def insert_tag():
    pass
    # upsert_list(cv.TAGS, 'tags')

def insert_data_type():
    pass
    # upsert_list(cv.TYPES, 'types')

def edit_type_schemas():
    pass
    # global __SCHEMA_PLACEHOLDER
    # query = Query()
    # schema_to_edit = None
    # data_types = __get_entries_list(cv.TYPES, 'types')
    # questions = {
    #     'type': 'list',
    #     'name': 'type',
    #     'message': 'Select a data type to edit.',
    #     'choices': data_types
    # }
    # answers = prompt(questions)
    # schema_to_edit = __get_schema(answers['type'])

    # print('The following schema exists for the {} type:\n'.format(answers['type']))
    # print(json.dumps(schema_to_edit, indent=4))

    # __SCHEMA_PLACEHOLDER = schema_to_edit
    forms.SCHEMA_MENU.show()