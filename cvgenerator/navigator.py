import cvgenerator as cv
import cvgenerator.wrappers.tinydb as __db
import cvgenerator.forms as forms
from cvgenerator.wrappers.pyinquirer import prompts

SCHEMA_CACHE = []

def start():
    #? Every remaining schema should be a child to this schema.
    #TODO add checks to ensure this raises an exception when more than one entry schema is found (Refactor get_schema)
    entry_schema = cv.DB_CLIENT.get_schema(1, key='nested_level')
    cycle_through_schemas(entry_schema)

def cycle_through_schemas(input_schema):
    # SCHEMA_CACHE.append(input_schema)
    # print(SCHEMA_CACHE)
    choice_array = []
    choice_array.append(prompts.get_separator('=====Parent====='))
    choice_array.append(input_schema['name'])
    choice_array.append(prompts.get_separator('====Children===='))
    for item in input_schema['children']:
        choice_array.append(item)

    selection_form = forms.get_navigator_menu(choice_array)
    answer = selection_form.show()
    
    if cv.IS_EXITED == False and not answer == selection_form.back_option.name:
        next_schema = cv.DB_CLIENT.get_schema(answer)
        cycle_through_schemas(next_schema)
    elif answer == selection_form.back_option.name:
        if not input_schema['parent'] == None:
            previous_schema = cv.DB_CLIENT.get_schema(input_schema['parent'])
            cycle_through_schemas(previous_schema)
    
    

#? For testing purposes:
if __name__ == "__main__":
    user_input = prompts.input_prompt('file', 'You are running the navigator tool directly.\n Please enter the file path for your \"./cv_bin/data/db.json\":', default='./cv_bin/data/db.json')
    cv.DB_CLIENT = __db.client(file_path = user_input)
