import yaml
import json
import importlib.resources as pkg_resources
from . import templates  # relative-import the *package* containing the templates
import cvgenerator as cv

SCHEMA_INDEX = []

def get_schema_template():
    return pkg_resources.read_text(templates, 'schemas_hierarchy.yaml')

def get_local_schema_template():
    '''
    Returns the schemas_hierarchy template in the cv_bin directory.
    '''
    with open('schemas_hierarchy.yaml', 'r') as file:
        contents = file.read()
    return contents

def get_schema_dict_from_file():
    contents_string = get_local_schema_template()
    contents_dict = yaml.safe_load(contents_string)
    keep_iterating = True
    values_array = []
    values_array.append(contents_dict)
    
    i = 0
    while keep_iterating == True:
        children_values = []

        for value in values_array:
            sub_values, sub_keys = get_children_keys(value)
            for sub_val in sub_values:
                children_values.append(sub_val)
            for sub in sub_keys:
                print('sublevel {} - {}'.format(i, sub))
            SCHEMA_INDEX.append({ i: sub_keys })

        keep_iterating = nested_keys_exist(values_array)
        values_array = children_values
        i += 1

    for entry in SCHEMA_INDEX:
        print(str(entry))

def nested_keys_exist(value_array: list):
    '''
    Returns True or False depending on whether a list or dict is present in the input list.
    '''
    output = False
    for value in value_array:
        if isinstance(value, dict) or isinstance(value, list):
            output = True
            break
    return output

# def get_parent_keys(input_obj):


def get_children_keys(input_obj):
    '''
    Constructs a list of child keys for further processing.
    '''
    output_values = []
    output_keys = None
    try:
        keys = __get_child_keys_if_dict(output_values, input_obj)
        if not keys == None:
            output_keys = keys
        elif isinstance(input_obj, list):
            keys_group = []
            for ob in input_obj:
                sub_keys = __get_child_keys_if_dict(output_values, ob)
                for key in sub_keys:
                    keys_group.append(key)
            output_keys = keys_group
    except Exception as e:
        print(str(e))
    return output_values, output_keys

def __get_child_keys_if_dict(input_list: list, instance):
    child_keys = None
    if isinstance(instance, dict):
        child_keys = []
        for key, value in instance.items():
            # print(key)
            child_keys.append(key)
            if not value == None:
                input_list.append(value)
    return child_keys

def get_default_parent_schema():
    return { 
        'type': None,
        'name': None,
        'parent': None,
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