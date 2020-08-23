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
    dict_array = []
    dict_array.append(contents_dict)
    
    i = 0
    while keep_iterating == True:
        children_dicts = []
        parent_keys = []

        for doc_obj in dict_array:
            if isinstance(doc_obj, dict):
                parent_keys = list(doc_obj.keys())
                for key in parent_keys:
                    if isinstance(doc_obj[key], dict) or isinstance(doc_obj[key], list):
                        children_dicts.append(doc_obj[key])
            elif isinstance(doc_obj, list):
                for sub_obj in doc_obj:
                    if isinstance(sub_obj, dict):
                        sub_parent_keys = sub_obj.keys()
                        if len(sub_parent_keys) == 1:
                            parent_keys.append(sub_parent_keys[0])
                            children_dicts.append(sub_obj)
            else:
                pass
                # print(type(doc_obj))1
        j = 0
        for item in children_dicts:
            pitem = item
            if isinstance(item, dict):
                pitem = list(item.keys())[0]
            print('''
            --------
            Level {}
            --------
            parent: {}
            children: {}
            --------
            '''.format(i, parent_keys[j], str(item)))
            j += 1

        dict_array = children_dicts
        keep_iterating = nested_keys_exist(dict_array)
        i += 1

    for entry in SCHEMA_INDEX:
        print(str(entry))

# def process_object(input_obj):
#     if isinstance(input_obj, dict):
#         keys, values = __process_dict(input_obj)
#     elif isinstance(input_obj, list):
#         pass
#     else:
#         print()

# def __process_dict(input: dict):

#     input.fromkeys()
    
#     return input.keys(), list(input.values())

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


# def get_children_keys(input_obj):
#     '''
#     Constructs a list of child keys for further processing.
#     '''
#     output_values = []
#     output_keys = None
#     try:
#         keys = __get_child_keys_if_dict(output_values, input_obj)
#         if not keys == None:
#             output_keys = keys
#         elif isinstance(input_obj, list):
#             keys_group = []
#             for ob in input_obj:
#                 sub_keys = __get_child_keys_if_dict(output_values, ob)
#                 for key in sub_keys:
#                     keys_group.append(key)
#             output_keys = keys_group
#     except Exception as e:
#         print(str(e))
#     return output_values, output_keys

# def __get_child_keys_if_dict(input_list: list, instance):
#     child_keys = None
#     if isinstance(instance, dict):
#         child_keys = []
#         for key, value in instance.items():
#             # print(key)
#             child_keys.append(key)
#             if not value == None:
#                 input_list.append(value)
#     return child_keys

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