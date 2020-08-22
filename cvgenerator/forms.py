import cvgenerator.workflows.editor as editor
import cvgenerator.workflows.utilities as utilities
import cvgenerator.workflows.schema as schema
from cvgenerator.wrappers.pyinquirer import menu, choice

CV_EDITOR_MENU = menu('cv_edit', 'What would you like to edit?')
CV_EDITOR_MENU.add_options([
    choice('Insert data entry', editor.insert_data),
    choice('Assign data tags', editor.assign_tags_to_data)
])

SCHEMA_MENU = menu('schema_edit', 'Options')
SCHEMA_MENU.add_options([
    choice('Add new schema', schema.add_new_schema),
    choice('Refresh schema hierarchy', schema.refresh_schema_hierarchy),
    choice('Edit existing schema', schema.edit_existing_schema),
    choice('View existing schemas', schema.view_existing_schemas)
])

MAIN_MENU = menu('main', 'What would you like to do?', escapable=False)
MAIN_MENU.add_options([
    choice('Compile my CV', CV_EDITOR_MENU.show),
    choice('Edit your CV', CV_EDITOR_MENU.show),
    choice('Data Utilities', SCHEMA_MENU.show)
])