def connect(db_type, database='todo_list', table='tasks'):
    if db_type == 'postgres':
        import clients.postgres_client as c
        return c.Client(database=database, table=table)
    
    elif db_type == 'mongodb':
        import clients.mongodb_client as c
        return c.Client(database=database, collection=table)
    
    elif db_type == 'mariadb':
        import clients.mariadb_client as c
        return c.Client(database=database, table=table)    
    
    elif db_type == 'mysql':
        import clients.mysql_client as c
        return c.Client(database=database, table=table)
