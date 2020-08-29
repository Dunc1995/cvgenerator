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

def edit_existing_schema():
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

# def add_new_schema():
#     adding_children = None
#     parent_schema = get_default_schema()
#     types_list = cv.DB_CLIENT.get_all_types()
#     first_child_prompt_prompted = False

#     ui_input_type = prompts.input_prompt('type', 'What name do you want to give your schema?')
#     if not ui_input_type in types_list:
#         parent_schema['type'] = ui_input_type
#         cv.DB_CLIENT.upsert_schema_entry('type', ui_input_type, parent_schema)

#         ui_children_yes_no = prompts.input_prompt('child_bool', 'Does your new schema have any children schemas? (y/n)\n For example, does it possess a start_date or end_date?')
#         if ui_children_yes_no == 'y':
#             while not adding_children == 'n':        
#                 if first_child_prompt_prompted == True:
#                     adding_children = prompts.input_prompt('continue', 'Continue adding children? (y/n)')

#                 if not adding_children == 'n':        
#                     ui_input_child_type = prompts.input_prompt('child', 'Please enter a name for the child schema.')
#                     parent_schema['children_types'].append(ui_input_child_type)
#                     cv.DB_CLIENT.upsert_schema_entry('type', ui_input_type, parent_schema)

#                     if ui_input_child_type in types_list:
#                         existing_child = cv.DB_CLIENT.get_schema(ui_input_child_type)
#                         existing_child['parent_types'].append(ui_input_type) #? adds the parent schema to its parent list
#                         cv.DB_CLIENT.upsert_schema_entry('type', ui_input_child_type, existing_child)
#                     else:
#                         child_schema = get_default_schema()
#                         child_schema['type'] = ui_input_child_type
#                         child_schema['parent_types'].append(ui_input_type)
#                         cv.DB_CLIENT.insert_schema(child_schema)

#                 first_child_prompt_prompted = True
#         else:
#             print('{} schema added!'.format(ui_input_type))
#     else:
#         print('{} schema already exists!'.format(ui_input_type))

def edit_default_schema_tags():
    navigator.start()

def edit_default_schema_names():
    print('Not implemented!')

def refresh_schema_hierarchy():
    should_continue = prompts.confirm('This will delete any default tags you have added to your data.\n Are you sure you want to continue?')

    if should_continue == True:
        schemas_list = parser.get_schemas_from_yaml()
        cv.DB_CLIENT.drop_schemas_table()
        for schema in schemas_list:
            cv.DB_CLIENT.insert_schema_entry(schema)
    else:
        print('Action cancelled.')