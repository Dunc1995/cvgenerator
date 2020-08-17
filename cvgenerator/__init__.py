#region #? Stateless
ROOT_DIRECTORY = 'cv_bin'
DEFAULT_SCHEMA = { 
        'type': None,
        'name': None,
        'contents': None,
        'parent': None, #? one to one relationship
        'parent_type': None, #? one to many relationship - one type could have many potential parent types.
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