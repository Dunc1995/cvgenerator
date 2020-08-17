from tinydb import TinyDB, Query

GENERIC_QUERY = Query()

class client():
    def __init__(self):
        self.db = TinyDB('./cv_db.json', sort_keys=True, indent=4, separators=(',', ': '))
        self.tags = self.db.table('tags')
        self.schemas = self.db.table('schemas')
        self.data = self.db.table('data')

    def get_all_types(self):
        '''
        Returns all existing data types in the database.
        '''
        return [ entry['type'] for entry in self.schemas.all() ]


    def __search(self, table: Table, key: str, value: str):
        return table.search(GENERIC_QUERY[key] == value)

#TODO refactor below
#region rubbish
def __get_entries_list(db_obj, list_name):
    query = Query()
    list_obj = None
    try:
        list_obj = db_obj.search(query.name == list_name)[0]['entries']
    except IndexError as e:
        list_obj = []
    return list_obj


def __get_schema(type_name: str):
    schema = None
    query = Query()
    try:
        schema = cv.SCHEMAS.search(query.type == type_name)[0]
    except IndexError as e:
        schema = cv.DEFAULT_SCHEMA
        schema['type'] = type_name
        cv.SCHEMAS.upsert(schema, query.type == type_name)
    return schema

def __upsert(table, dict_input, name, key = 'name'):
        table.upsert(dict_input, Query()[key] == name)

def upsert_list(db_obj, list_name : str):
    query = Query()
    list_obj = __get_entries_list(db_obj, list_name)
    list_name_singular = list_name[:-1]

    questions = {
        'type': 'input',
        'name': list_name_singular,
        'message': 'Enter a new {} name.'.format(list_name_singular),
    }
    answers = prompt(questions)
    list_obj.append(answers[list_name_singular])

    db_obj.upsert({'name': list_name, 'entries': list_obj}, query.name == list_name)
#endregion