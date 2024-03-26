from psycopg2 import connect
from psycopg2.extensions import Column
import os

# DATABASE_URL = os.environ['DATABASE_URL']
DATABASE_URL = '${{ Postgres.DATABASE_URL }}'

class Client:
    def __init__(self, database: str, table: str, host='localhost', port='5432'):
        self.connection = connect(DATABASE_URL, sslmode='require', user='postgres', password='') #host=host, port=port, database=database, 
                                  
        self.cursor = self.connection.cursor()
        self.table = table
    
    def __exit__(self):
        self.connection.close()

    def __convert_to_dict(self, rv):
        row_headers = [x[0] for x in self.cursor.description]
        return [dict(zip(row_headers, row_values)) for row_values in rv]

    def get_all(self):
        sql = f'select * from {self.table} order by id'
        self.cursor.execute(sql)
        rv =  self.cursor.fetchall()
        return self.__convert_to_dict(rv)

    def insert_one(self, params: dict) -> bool:
        # create string of values and keys
        vals = '('
        keys = '('
        for key, val in params.items():
            if val is not None:
                vals += f"'{str(val)}',"
                keys += key+','
        vals = vals[:-1]
        keys = keys[:-1]
        vals += ')'
        keys += ')'

        sql = f'INSERT INTO {self.table} {keys} VALUES {vals} RETURNING id'
        self.cursor.execute(sql)
        self.connection.commit()
        result = self.cursor.fetchone()
        if result:
            return True
        return False

    def update_by_id(self, params: dict, id) -> bool:
        sets = ''
        for key, val in params.items():
            if val is not None:
                sets += f"{key} = '{str(val)}',"
        sets = sets[:-1]
        sql = f'UPDATE {self.table} SET {sets} WHERE id = {id} RETURNING id'
        self.cursor.execute(sql)
        self.connection.commit()
        result = self.cursor.fetchone()
        if result:
            return True
        return False
    
    def delete_by_id(self, id) -> bool:
        sql = f'DELETE FROM {self.table} WHERE id = {id} RETURNING id'
        self.cursor.execute(sql)
        self.connection.commit()
        result = self.cursor.fetchone()
        if result:
            return True
        return False
    
