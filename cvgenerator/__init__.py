#region #? Stateless
ROOT_DIRECTORY = 'cv_bin'
DEFAULT_SCHEMA = { 
        'type': None,
        'name': None,
        'contents': None,
        'parent': None, #? one to one relationship
        'parent_types': [], #? one to many relationship - one type could have many potential parent types.
        'children_types': [],
        'tags': [] 
        }
#endregion

#region #? Stateful
IS_EXITED = False
DB_CLIENT = None
#endregion