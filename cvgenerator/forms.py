from cvgenerator.workflows import utilities
from cvgenerator.wrappers.pyinquirer import menu, choice

def placeholder():
    print('Not yet implemented')

COMPILER_MENU = menu('compile', 'Please select an option.')
COMPILER_MENU.add_choices([
    choice('', placeholder),
    choice('Select tag preferences', placeholder)
])

EDITOR_MENU = menu('edit', 'What would you like to edit?')
EDITOR_MENU.add_choices([
    choice('Browse data', placeholder),
    choice('Insert data', placeholder),
    choice('Update existing data', placeholder),
    choice('Remove existing data', placeholder),
    choice('Help', placeholder)
])

UTILITIES_MENU = menu('utilities', 'Options')
UTILITIES_MENU.add_choices([
    choice('Edit default schema names', utilities.edit_default_schema_names),
    choice('Edit default schema tags', utilities.edit_default_schema_tags),
    choice('Edit schema hierarchy config', utilities.edit_schema_hierarchy),
    choice('Edit tag options config', utilities.edit_tag_options),
    choice('Refresh schema hierarchy', utilities.refresh_schema_hierarchy),
    choice('Test', utilities.test),
    choice('Help', utilities.show_help)
])

MAIN_MENU = menu('main', 'What would you like to do?', escapable=False)
MAIN_MENU.add_choices([
    choice('Generate my CV', COMPILER_MENU.show),
    choice('Edit your CV', EDITOR_MENU.show),
    choice('Data Utilities', UTILITIES_MENU.show)
])

#! This is jenky and probably very breakable.
def get_navigator_menu(input_array: list):
    choice_array = []
    navigator_menu = menu('navigate', 'Please select a schema:\n')
    for item in input_array:
        if not type(item) is choice:
            choice_array.append(choice(item))
        else:
            choice_array.append(item)
    navigator_menu.add_choices(choice_array)
    return navigator_menu