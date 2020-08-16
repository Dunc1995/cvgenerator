import cvgenerator.workflows as wf
from cvgenerator.forms import menu, choice

#region #? Stateless
ROOT_DIRECTORY = 'cv_bin'

EDIT_MENU = menu('edit', 'What would you like to create?')
EDIT_MENU.add_options([
    choice('Insert data entry', wf.insert_data),
    choice('Insert new tag', wf.insert_tag),
    choice('Insert new data type', wf.insert_data_type),
    choice('Edit data type schemas', wf.edit_type_schemas),
    choice('Assign data tags', wf.assign_tags_to_data)
])

MAIN_MENU = menu('main', 'What would you like to do?', escapable=False)
MAIN_MENU.add_options([
    choice('Compile my CV', wf.placeholder),
    choice('Edit CV Data', EDIT_MENU.show)
])

DEFAULT_SCHEMA = { 
        'type': None,
        'name': None,
        'contents': None,
        'parent': None, #? one to one relationship
        'type_parent': None, #? one to many relationship - one type could have many potential parent types.
        'tags': [] }
#endregion

#region #? Stateful
IS_EXITED = False
DB_OBJ = None
TYPES = None
TAGS = None
SCHEMAS = None
DATA = None
#endregion