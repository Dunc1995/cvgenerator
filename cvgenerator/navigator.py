import cvgenerator as cv
import cvgenerator.wrappers.tinydb as __db
from cvgenerator.wrappers.pyinquirer import prompts

def start():
    #? Every remaining schema should be a child to this schema.
    #TODO add checks to ensure this raises an exception when more than one entry schema is found (Refactor get_schema)
    entry_schema = cv.DB_CLIENT.get_schema(1, key='nested_level')
    cycle_through_schemas(entry_schema)

def cycle_through_schemas(input_schema):
    exit = False
    while exit == False:
        selection_array = input_schema['children']
        selection_array.append(prompts.get_separator())
        selection_array.append('<<< Back')
        selection_array.append('<X> Exit')

        user_selection = prompts.list_prompt(input_schema['type'], 'Please select a schema:\n', selection_array )
        
        if user_selection == '<X> Exit':
            exit = True
        else:
            cycle_through_schemas(cv.DB_CLIENT.get_schema(user_selection))

#? For testing purposes:
if __name__ == "__main__":
    user_input = prompts.input_prompt('file', 'You are running the navigator tool directly.\n Please enter the file path for your \"./cv_bin/data/db.json\":', default='./cv_bin/data/db.json')
    cv.DB_CLIENT = __db.client(file_path = user_input)
