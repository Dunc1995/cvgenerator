import importlib.resources as pkg_resources
from . import templates  # relative-import the *package* containing the templates

def get_schema_template():
    return pkg_resources.read_text(templates, 'schemas_hierarchy.yaml')
