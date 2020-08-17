from cvgenerator.workflows import editor, schema, utilities, not_implemented

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
    choice('Compile my CV', not_implemented),
    choice('Edit your CV', CV_EDITOR_MENU.show),
    choice('Data Utilities', UTILITIES_MENU.show)
])

SCHEMA_MENU = menu('schema_edit', 'Options')
SCHEMA_MENU.add_options([
    choice('Add parameter', schema.add_schema_key),
    choice('Remove parameter', schema.remove_schema_key),
    choice('Add data type parent', schema.add_type_parent),
    choice('Remove data type parent', schema.remove_type_parent)
])