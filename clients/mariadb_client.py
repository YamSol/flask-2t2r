from mariadb import connect

class Client:
    def __init__(self, database: str, table: str, host = '172.17.0.3', port=3306):
        self.connection = connect(host=host, port=port, database=database, 
                                  user='root', password='mariadb')
        self.cursor = self.connection.cursor()
        self.table = table

    def __exit__(self):
        self.connection.close()

    def insert_one(self, value: str) -> bool:
        sql = f'INSERT INTO {self.table} (name, checked) VALUES (%s, false)'
        self.cursor.execute(sql, (value, ))
        self.connection.commit()
        if self.cursor.rowcount > 0:
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
        sql = f'UPDATE {self.table} SET {value_name} = %s WHERE id = %s'
        self.cursor.execute(sql, (value, id))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            return True
        return False
    
    def delete_by_id(self, id: str) -> bool:
        sql = f'DELETE FROM {self.table} WHERE id = %s'
        self.cursor.execute(sql, (id, ))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            return True
        return False
         