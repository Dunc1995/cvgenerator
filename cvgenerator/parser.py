import yaml
import json
import importlib.resources as pkg_resources
from . import templates  # relative-import the *package* containing the templates
import cvgenerator as cv

schema_index = 1

def get_pkg_file(file_name: str):
    '''Loads the input file name from the python package.'''
    return pkg_resources.read_text(templates, file_name)

def get_local_file(file_name: str):
    '''Returns the local file in the cv_bin directory.'''
    with open(file_name, 'r') as file:
        contents = file.read()
    return contents

def get_all_values(nested_dictionary, input_list, index=0, parent_key=None):
    '''Propagates through every key value pair in an input dict, then appends each key and its properties to the SCHEMAS list in __init__.py.'''
    __child_keys = []
    append_keys = []
    nested_index = index+1
    global schema_index

    for key, value in nested_dictionary.items():
        is_list = False
        __child_keys.append(key)
        append_keys.clear()
        
        if type(value) is dict:
            append_keys = get_all_values(value, input_list, index=nested_index, parent_key=key)
        elif type(value) is list:
            append_keys = []
            is_list = True
            for item in value:
                __sub_group = get_all_values(item, input_list, index=nested_index, parent_key=key)
                for i in __sub_group:
                    append_keys.append(i)
        else:
            pass
            # print(key, ":", value)

        schema = get_default_schema()
        schema['type'] = key
        schema['name'] = key.replace('_', ' ').title()
        schema['listable_children'] = is_list
        schema['nested_level'] = nested_index
        schema['parent'] = parent_key

        if not append_keys == None and len(append_keys) > 0:
            #TODO add this print method to a logger
            # print('''
            # parent: {}
            # children: {}
            # '''.format(key, append_keys))
            schema['base_type'] = 'parent'
            for entry in append_keys:
                schema['children'].append(entry)
        elif append_keys == None or len(append_keys) == 0:
            schema['base_type'] = 'child'
        #TODO could with some validation before appending
        input_list.append(schema)
        print('name: {}, index: {}'.format(key, schema_index))
        schema_index += 1
    return __child_keys

def get_schemas_from_yaml():
    '''Parses the schemas_hierarchy.yaml contents and creates dicts for each data type.'''
    schemas_list = []
    contents_string = get_local_file(cv.SCHEMAS_PATH)
    contents_dict = yaml.safe_load(contents_string)
    get_all_values(contents_dict, schemas_list)
    return schemas_list

def get_tags_from_yaml():
    '''Parses the default_tags.yaml contents.'''
    schemas_list = []
    contents_string = get_local_file(cv.TAGS_PATH)
    contents_dict = yaml.safe_load(contents_string)
    return contents_dict

def get_default_schema():
    return { 
        'type': None,
        'base_type': None,
        'parent': None,
        'name': None,
        'children': [],
        'tags': [],
        'listable_children': False,
        'nested_level': None
        }