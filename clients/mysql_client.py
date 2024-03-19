# from psycopg2 import connect
import MySQLdb

class Client():
    def __init__(self, database: str, table: str, host = 'localhost', port=3306):
        self.connection = MySQLdb.connect(host=host, port=port, user='root', 
                                          password='DWH&Thi34u$JOH&', database=database)
        self.cursor = self.connection.cursor()
        self.table = table
    
    def __exit__(self):
         self.connection.close()

    def insert_one(self, value: str):
        sql = f'INSERT INTO {self.table} (name, checked) VALUES (\'{value}\', false)'
        self.cursor.execute(sql)
        self.connection.commit()
    
    def get_all(self):
        sql = f'select * from {self.table}'
        self.cursor.execute(sql)
        # row_headers = [x[0] for x in self.cursor.description]
        rv =  self.cursor.fetchall()
        return rv
        json_data = [dict(zip(row_headers, row_values)) for row_values in rv]
        return json_data

    def update_by_id(self, value_name: str, value: str, id: str):
        # connection.commit() é necessário
        sql = f'UPDATE {self.table} SET {value_name} = \'{value}\' WHERE id = {id}'
        self.cursor.execute(sql)
        self.connection.commit()
    
    def delete_by_id(self, id: str):
         sql = f'DELETE FROM {self.table} WHERE id = {id}'
         self.cursor.execute(sql)
         self.connection.commit()
         result = self.cursor.fetchall()
         return result
    