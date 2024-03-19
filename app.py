from flask import Flask, request
import sys
# import json
# from bson import ObjectId
import database_connect


app = Flask(__name__)
app.config["DEBUG"] = True

# def get_terminal_db_type():
db_types = ['postgres',
            'mongodb',
            'mariadb',
            'mysql'
            ]

db_type = db_types[0]; # default value

if '--db-type' in sys.argv:
    next = sys.argv.index('--db-type') + 1
    if sys.argv[next] in db_types:
        db_type = sys.argv[next]
        
print(f'{db_type.upper()} SELECTED!')
    
    # return selected_db_type;


@app.get('/')
def main():
    client = database_connect.connect(db_type=db_type)
    recset = client.get_all()
    if recset:
        return recset 
    return {}, 404

# @app.get('/graphql')
# def graphql():
#     return 200

@app.post('/')
def create():
    client = database_connect.connect(db_type=db_type)
    name = request.json.get('name')
    response = client.insert_one(name)
    if response:
        return {}, 201
    return {}, 404

@app.put('/')
def update():
    client = database_connect.connect(db_type=db_type)

    id = request.args.get('id', type=int)

    checked = request.json.get('checked')
    name = request.json.get('name')

    if checked is not None:
        # if checked in ['0', 0, 'false', 'False', False]:
        #     checked = '0'
        # if checked in ['1', 1, 'true', 'True', True]:
        #     checked = '1'
        response = client.update_by_id(value_name='checked', value=checked, id=id)

    if name is not None:
        response = client.update_by_id(value_name='name', value=name, id=id)
    
    if response:
        return {}, 204
    return {}, 404

@app.delete('/')
def delete():
    id = request.args.get('id', type=int)
    client = database_connect.connect(db_type=db_type)
    response = client.delete_by_id(id=id)
    if response:
        return {}, 204 # For a DELETE request: HTTP 200 or HTTP 204 should imply "resource deleted successfully".
    return {}, 404

if __name__ == "__main__":
    app.run()
