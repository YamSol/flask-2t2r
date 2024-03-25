from psycopg2 import connect
from psycopg2.extensions import Column

class Client:
    def __init__(self, database: str, table: str, host='localhost', port='5432'):
        self.connection = connect(host=host, port=port, database=database, 
                                  user='postgres', password='')
        self.cursor = self.connection.cursor()
        self.table = table
    
    def __exit__(self):
        self.connection.close()
 
    def insert_one(self, value: str) -> bool:
        sql = f'INSERT INTO {self.table} (name, checked) VALUES (\'%s\', false) RETURNING id'
        self.cursor.execute(sql, (value))
        self.connection.commit()
        result = self.cursor.fetchone()
        if result:
            return True
        return False
    
    def __convert_to_dict(self, rv):
        row_headers = [x[0] for x in self.cursor.description]
        return [dict(zip(row_headers, row_values)) for row_values in rv]

    def get_all(self):
        sql = f'select * from {self.table}'
        self.cursor.execute(sql)
        rv =  self.cursor.fetchall()
        return self.__convert_to_dict(rv)

    def update_by_id(self, value_name: str, value: str, id: str) -> bool:
        sql = f'UPDATE {self.table} SET %s = %s WHERE id = %s RETURNING id'
        self.cursor.execute(sql, (value_name, value, id, ))
        self.connection.commit()
        result = self.cursor.fetchone()
        if result:
            return True
        return False
    
    def delete_by_id(self, id: str) -> bool:
        sql = f'DELETE FROM {self.table} WHERE id = %s RETURNING id'
        self.cursor.execute(sql, (id))
        self.connection.commit()
        result = self.cursor.fetchone()
        if result:
            return True
        return False
    
