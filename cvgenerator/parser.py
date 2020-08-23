import yaml
import json
import importlib.resources as pkg_resources
from . import templates  # relative-import the *package* containing the templates

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
        print('''
        --------
        Level {}
        --------
        '''.format(i))
        
        children_values = []
        for value in values_array:
            sub_values = get_children_keys(value)
            for sub_val in sub_values:
                children_values.append(sub_val)
        keep_iterating = nested_dict_exists(values_array)
        values_array = children_values
        i += 1

def nested_dict_exists(value_array: list):
    '''
    Returns True or False depending on whether a list or dict is present in the input list.
    '''
    output = False
    for value in value_array:
        if isinstance(value, dict) or isinstance(value, list):
            output = True
            break
    return output

def get_children_keys(input_obj):
    '''
    Constructs a list of child keys for further processing.
    '''
    #!-----------------------------------
    #!This is is likely to be problematic
    #!-----------------------------------
    output = []
    try:
        if isinstance(input_obj, dict):
            for key, value in input_obj.items():
                print(key)
                if not value == None:
                    output.append(value)
                else:
                    output.append(key)
        elif isinstance(input_obj, list):
            for ob in input_obj:
                if isinstance(ob, dict): #TODO could put this if statement into its own method to avoid code repetition
                    for key, value in ob.items():
                        print(key)
                        if not value == None:
                            output.append(value)
                        else:
                            output.append(key)
        else:
            print(str(input_obj))
    except Exception as e:
        print(str(e))
    return output