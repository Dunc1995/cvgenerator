from tinydb import TinyDB, Query

class client():
    def __init__(self, file_path='./data/db.json'):
        self.db = TinyDB(file_path, sort_keys=True, indent=4, separators=(',', ': '))
        self.tags = self.db.table('tags')
        self.schemas = self.db.table('schemas')
        self.data = self.db.table('data')
        self.query = Query()

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

    def get_schema_by_uid(self, uid: str):
        result = self.get_object_by_uid('schemas', uid)
        return result

    def get_parent_schema(self):
        result = self.get_parent_object('schemas')
        return result

    def get_object_by_uid(self, table: str, uid: str):
        '''Gets a db object by its unique identifier. Raises an exception if it finds more than one object with the same id.'''
        output = None
        object_array = self.db.table(table).search(self.query['unique_id'] == uid)
        if len(object_array) == 1:
            output = object_array[0]
        elif len(object_array) > 1:
            raise Exception('Found objects with duplicate id\'s!')
        else:
            raise Exception('Object with unique_id \"{}\" not found.'.format(uid))

        return output

    def get_parent_object(self, table: str):
        '''Gets a db object by its unique identifier. Raises an exception if it finds more than one object with the same id.'''
        output = None
        object_array = self.db.table(table).search(self.query['parent'] == None)
        if len(object_array) == 1:
            output = object_array[0]
        elif len(object_array) > 1:
            raise Exception('Found too many parent objects!')
        else:
            raise Exception('Found no entry point for the document.')

        return output

    def search(self, table, key: str, value: str):
        return table.search(self.query[key] == value)

    def insert_schema_entry(self, schema: dict):
        self.schemas.insert(schema)

    def insert_tags(self, tags: dict):
        self.tags.insert(tags)

    #! Refactor this rubbish
    def upsert_tag_entry(self, key: str, value: str, data: dict):
        self.tags.upsert(data, self.query[key] == value)

    def upsert_schema_entry(self, key: str, value: str, data: dict):
        self.schemas.upsert(data, self.query[key] == value)

    def upsert_data_entry(self, key: str, value: str, data: dict):
        self.data.upsert(data, self.query[key] == value)

    def drop_table(self, table_name: str):
        self.db.drop_table(table_name)
