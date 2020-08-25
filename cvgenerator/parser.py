import yaml
import json
import importlib.resources as pkg_resources
from . import templates  # relative-import the *package* containing the templates
import cvgenerator as cv

def get_schema_template():
    return pkg_resources.read_text(templates, 'schemas_hierarchy.yaml')

def get_local_schema_template():
    '''
    Returns the schemas_hierarchy template in the cv_bin directory.
    '''
    with open('schemas_hierarchy.yaml', 'r') as file:
        contents = file.read()
    return contents

def get_all_values(nested_dictionary):
    __child_keys = []
    append_keys = []

    for key, value in nested_dictionary.items():
        __child_keys.append(key)
        append_keys.clear()

        if type(value) is dict:
            append_keys = get_all_values(value)
        elif type(value) is list:
            append_keys = []
            for item in value:
                __sub_group = get_all_values(item)
                for i in __sub_group:
                    append_keys.append(i)
        else:
            pass
            # print(key, ":", value)
        if not append_keys == None and len(append_keys) > 0:
            print('''
            parent: {}
            children: {}
            '''.format(key, append_keys))
            schema = get_default_parent_schema()
            schema['type'] = key
            for entry in append_keys:
                schema['children'].append(entry)
            cv.SCHEMAS.append(schema)
        


    
    return __child_keys

def get_schema_dict_from_file():
    contents_string = get_local_schema_template()
    contents_dict = yaml.safe_load(contents_string)
    get_all_values(contents_dict)
    return cv.SCHEMAS

def get_default_parent_schema():
    return { 
        'type': None,
        'name': None,
        'children': [],
        'tags': []
        }

def get_default_schema():
    return { 
        'type': None,
        'name': None,
        'value': None,
        'parent': None,
        'tags': []
        }