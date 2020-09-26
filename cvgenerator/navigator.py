import cvgenerator as cv
import cvgenerator.wrappers.tinydb as __db #? this is only needed when running 'python -i navigator.py'
import cvgenerator.forms as forms
from cvgenerator.wrappers.pyinquirer import prompts, choice
import os

SCHEMA_CACHE = []
CACHED_SCHEMA = None
CACHED_DOC = None

def start():
    #? Every remaining schema should be a child to this schema.
    entry_schema = cv.DB_CLIENT.get_parent_schema()
    cycle_through_schemas(entry_schema)

def walk_through_data():
    global CACHED_DOC
    CACHED_DOC = ''
    entry_schema = cv.DB_CLIENT.get_parent_schema()
    __walk_through_data(entry_schema)
    print(CACHED_DOC)

def __walk_through_data(input_schema):
    global CACHED_DOC

    if input_schema['base_type'] == 'parent':
        CACHED_DOC += '{} {}\n\n'.format(input_schema['nested_level']*'#', input_schema['name'])
        for item in input_schema['children']:
            schema_object = cv.DB_CLIENT.get_schema_by_uid(item)
            __walk_through_data(schema_object)
        CACHED_DOC += '\n'
    elif input_schema['base_type'] == 'child':
        CACHED_DOC += '- {}\n'.format(input_schema['name'])

def cycle_through_schemas(input_schema):
    # SCHEMA_CACHE.append(input_schema)
    # print(SCHEMA_CACHE)
    os.system('clear')
    global CACHED_SCHEMA
    CACHED_SCHEMA = input_schema

    result = None
    schema_objects = []
    choice_array = []
    choice_array.append(prompts.get_separator('=====Parent====='))
    choice_array.append(choice(input_schema['name'], __tag_selection_prompt))

    if input_schema['base_type'] == 'parent':
        choice_array.append(prompts.get_separator('====Children===='))

        for item in input_schema['children']:
            schema_object = cv.DB_CLIENT.get_schema_by_uid(item)
            schema_objects.append(schema_object)
            choice_array.append(schema_object['name'])

        selection_form = forms.get_navigator_menu(choice_array)
        answer = selection_form.show()
        
        for item in schema_objects:
            if item['name'] == answer:
                result = item
                break
        
        if cv.IS_EXITED == False and not answer == selection_form.back_option.name:
            next_schema = cv.DB_CLIENT.get_schema_by_uid(result['unique_id'])
            cycle_through_schemas(next_schema)
        elif answer == selection_form.back_option.name:
            if not input_schema['parent'] == None:
                previous_schema = cv.DB_CLIENT.get_schema_by_uid(input_schema['parent'])
                cycle_through_schemas(previous_schema)
    else:
        __tag_selection_prompt()


def __tag_selection_prompt():
    global CACHED_SCHEMA
    input_schema = CACHED_SCHEMA

    tags_array = cv.DB_CLIENT.get_all_tags()
    tags_menu = []

    for tag in tags_array:
        if tag in input_schema['tags']:
            tags_menu.append({
                'name': tag,
                'checked': True 
            })
        else:
            tags_menu.append({
                'name': tag
            })

    tag_selection = prompts.checkbox(tags_menu, 'Select your tags for {}'.format(input_schema['type']))

    input_schema['tags'] = tag_selection
    cv.DB_CLIENT.upsert_schema_entry('unique_id', input_schema['unique_id'], input_schema)
    previous_schema = cv.DB_CLIENT.get_schema_by_uid(input_schema['parent'])
    cycle_through_schemas(previous_schema)

#? For testing purposes:
if __name__ == "__main__":
    user_input = prompts.input_prompt('file', 'You are running the navigator tool directly.\n Please enter the file path for your \"./cv_bin/data/db.json\":', default='./cv_bin/data/db.json')
    cv.DB_CLIENT = __db.client(file_path = user_input)
