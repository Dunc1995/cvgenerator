import cvgenerator.forms as forms
import cvgenerator as cv
from cvgenerator.wrappers.pyinquirer import prompts
import json

def get_default_schema():
    '''
    Returns a blank schema for manipulation. This is a workaround to avoid mutability issues with list objects and Python's weirdness.
    '''
    return { 
        'type': None,
        'name': None,
        'contents': None,
        'parent': None, #? one to one relationship
        'parent_types': [], #? one to many relationship - one type could have many potential parent types.
        'children_types': [],
        'tags': [] 
        }

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
    # forms.SCHEMA_MENU.show()

def add_new_schema():
    adding_children = None
    parent_schema = get_default_schema()
    types_list = cv.DB_CLIENT.get_all_types()
    first_child_prompt_prompted = False

    ui_input_type = prompts.input_prompt('type', 'What name do you want to give your schema?')
    if not ui_input_type in types_list:
        parent_schema['type'] = ui_input_type
        cv.DB_CLIENT.upsert_schema_entry('type', ui_input_type, parent_schema)

        ui_children_yes_no = prompts.input_prompt('child_bool', 'Does your new schema have any children schemas? (y/n)\n For example, does it possess a start_date or end_date?')
        if ui_children_yes_no == 'y':
            while not adding_children == 'n':        
                if first_child_prompt_prompted == True:
                    adding_children = prompts.input_prompt('continue', 'Continue adding children? (y/n)')

                if not adding_children == 'n':        
                    ui_input_child_type = prompts.input_prompt('child', 'Please enter a name for the child schema.')
                    parent_schema['children_types'].append(ui_input_child_type)
                    cv.DB_CLIENT.upsert_schema_entry('type', ui_input_type, parent_schema)

                    if ui_input_child_type in types_list:
                        existing_child = cv.DB_CLIENT.get_schema(ui_input_child_type)
                        existing_child['parent_types'].append(ui_input_type) #? adds the parent schema to its parent list
                        cv.DB_CLIENT.upsert_schema_entry('type', ui_input_child_type, existing_child)
                    else:
                        child_schema = get_default_schema()
                        child_schema['type'] = ui_input_child_type
                        child_schema['parent_types'].append(ui_input_type)
                        cv.DB_CLIENT.insert_schema(child_schema)

                first_child_prompt_prompted = True
        else:
            print('{} schema added!'.format(ui_input_type))
    else:
        print('{} schema already exists!'.format(ui_input_type))

def add_schema_key():
    pass
    # global __SCHEMA_PLACEHOLDER
    # query = Query()
    # new_key = forms.input_prompt('key', 'Please enter a key name')
    # __SCHEMA_PLACEHOLDER[new_key] = None
    # cv.SCHEMAS.upsert(__SCHEMA_PLACEHOLDER, query.type == __SCHEMA_PLACEHOLDER['type'])

def remove_schema_key():
    pass
    # global __SCHEMA_PLACEHOLDER
    # query = Query()
    # questions = {
    #     'type': 'list',
    #     'name': 'key',
    #     'message': 'Please select a key to remove.',
    #     'choices': __SCHEMA_PLACEHOLDER.keys()
    # }
    # answer = prompt(questions)
    
    #__SCHEMA_PLACEHOLDER[answer['key']] = None
    #cv.SCHEMAS.upsert(__SCHEMA_PLACEHOLDER, query.type == __SCHEMA_PLACEHOLDER['type'])

def add_type_parent():
    pass
    # placeholder()

def remove_type_parent():
    pass
    # placeholder()

def view_existing_schemas():
    types = cv.DB_CLIENT.get_all_types()
    for schema_type in types:
        print(schema_type)

