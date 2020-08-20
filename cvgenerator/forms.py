import cvgenerator.workflows.editor as editor
import cvgenerator.workflows.utilities as utilities
import cvgenerator.workflows.schema as schema
from cvgenerator.wrappers.pyinquirer import menu, choice

CV_EDITOR_MENU = menu('cv_edit', 'What would you like to edit?')
CV_EDITOR_MENU.add_options([
    choice('Insert data entry', editor.insert_data),
    choice('Assign data tags', editor.assign_tags_to_data)
])

UTILITIES_MENU = menu('data_edit', 'What would you like to edit?')
UTILITIES_MENU.add_options([
    choice('Insert new tag', utilities.insert_tag),
    choice('Insert new data type', utilities.insert_data_type),
    choice('Edit data type schemas', utilities.edit_type_schemas)
])

MAIN_MENU = menu('main', 'What would you like to do?', escapable=False)
MAIN_MENU.add_options([
    choice('Compile my CV', CV_EDITOR_MENU.show),
    choice('Edit your CV', CV_EDITOR_MENU.show),
    choice('Data Utilities', UTILITIES_MENU.show)
])

SCHEMA_MENU = menu('schema_edit', 'Options')
SCHEMA_MENU.add_options([
    choice('Add new schema', schema.add_new_schema),
    choice('View existing schemas', schema.view_existing_schemas)
])