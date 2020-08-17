CV_EDITOR_MENU = menu('cv_edit', 'What would you like to edit?')
CV_EDITOR_MENU.add_options([
    choice('Insert data entry', wf.insert_data),
    choice('Assign data tags', wf.assign_tags_to_data)
])

UTILITIES_MENU = menu('data_edit', 'What would you like to edit?')
UTILITIES_MENU.add_options([
    choice('Insert new tag', wf.insert_tag),
    choice('Insert new data type', wf.insert_data_type),
    choice('Edit data type schemas', wf.edit_type_schemas)
])

MAIN_MENU = menu('main', 'What would you like to do?', escapable=False)
MAIN_MENU.add_options([
    choice('Compile my CV', wf.placeholder),
    choice('Edit your CV', CV_EDITOR_MENU.show),
    choice('Data Utilities', UTILITIES_MENU.show)
])

SCHEMA_MENU = menu('schema_edit', 'Options')
SCHEMA_MENU.add_options([
    choice('Add parameter', wf.add_schema_key),
    choice('Remove parameter', wf.remove_schema_key),
    choice('Add data type parent', wf.add_type_parent),
    choice('Remove data type parent', wf.remove_type_parent)
])