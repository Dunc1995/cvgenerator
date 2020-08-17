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