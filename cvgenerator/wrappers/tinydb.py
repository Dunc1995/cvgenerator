from tinydb import TinyDB, Query

GENERIC_QUERY = Query()

class client():
    def __init__(self, file_path='./data/db.json'):
        self.db = TinyDB(file_path, sort_keys=True, indent=4, separators=(',', ': '))
        self.tags = self.db.table('tags')
        self.schemas = self.db.table('schemas')
        self.data = self.db.table('data')

    def get_all_types(self):
        '''
        Returns all existing data types in the database.
        '''
        return [ entry['type'] for entry in self.schemas.all() ]

    def get_all_tags(self):
        list_obj = None
        try:
            list_obj = self.tags.all()[0]['tags']
        except IndexError as e:
            list_obj = []
        return list_obj

    def get_schema(self, value: str, key='type'):
        schema = None
        try:
            schema = self.schemas.search(GENERIC_QUERY[key] == value)[0] #! DONT LEAVE THIS HERE!
        except IndexError as e:
            schema = None
        return schema

    def search(self, table, key: str, value: str):
        return table.search(GENERIC_QUERY[key] == value)

    def insert_schema_entry(self, schema: dict):
        self.schemas.insert(schema)

    def insert_tags(self, tags: dict):
        self.tags.insert(tags)

    #! Refactor this rubbish
    def upsert_tag_entry(self, key: str, value: str, data: dict):
        self.tags.upsert(data, GENERIC_QUERY[key] == value)

    def upsert_schema_entry(self, key: str, value: str, data: dict):
        self.schemas.upsert(data, GENERIC_QUERY[key] == value)

    def upsert_data_entry(self, key: str, value: str, data: dict):
        self.data.upsert(data, GENERIC_QUERY[key] == value)

    def drop_table(self, table_name: str):
        self.db.drop_table(table_name)
