#region #? Stateless
import os
import cvgenerator as cv

ROOT_DIRECTORY = 'cv_bin'
SCHEMAS_PATH = os.path.join('config', 'schemas_hierarchy.yaml')
TAGS_PATH = os.path.join('config', 'default_tags.yaml')
#endregion

#region #? Stateful
IS_EXITED = False
DB_CLIENT = None
#endregion