import cvgenerator.workflows.editor as editor
import cvgenerator.workflows.utilities as utilities
from cvgenerator.wrappers.pyinquirer import menu, choice

def placeholder():
    print('Not yet implemented')

COMPILER_MENU = menu('compile', 'Please select an option.')
COMPILER_MENU.add_options([
    choice('', placeholder),
    choice('Select tag preferences', placeholder)
])

EDITOR_MENU = menu('edit', 'What would you like to edit?')
EDITOR_MENU.add_options([
    choice('Browse data', placeholder),
    choice('Insert data', editor.test),
    choice('Update existing data', placeholder),
    choice('Remove existing data', placeholder),
    choice('Help', placeholder)
])

UTILITIES_MENU = menu('utilities', 'Options')
UTILITIES_MENU.add_options([
    choice('Edit default schema names', utilities.edit_default_schema_names),
    choice('Edit default schema tags', utilities.edit_default_schema_tags),
    choice('Refresh schema hierarchy', utilities.refresh_schema_hierarchy),
    choice('Help', utilities.show_help)
])

MAIN_MENU = menu('main', 'What would you like to do?', escapable=False)
MAIN_MENU.add_options([
    choice('Generate my CV', COMPILER_MENU.show),
    choice('Edit your CV', EDITOR_MENU.show),
    choice('Data Utilities', UTILITIES_MENU.show)
])

def get_navigator_menu(input_array: list):
    choice_array = []
    navigator_menu = menu('navigate', 'Please select a schema:\n')
    for name in input_array:
        choice_array.append(name)
    navigator_menu.add_options(choice_array)
    return navigator_menu