from flask import Flask, request
import sys
import database_connect

app = Flask(__name__)
app.config["DEBUG"] = True

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

@app.get('/')
def main():
    return {}
    client = database_connect.connect(db_type=db_type)

    recset = client.get_all()
    if recset:
        return recset, 200
    return {}, 404

@app.post('/')
def create():
    client = database_connect.connect(db_type=db_type)
    
    params = {}
    params['name'] = request.json.get('name')
    params['checked'] = request.json.get('checked')
    params['id'] = request.json.get('id')

    response = client.insert_one(params=params)
    if response:
        return {}, 201
    return {}, 404

@app.put('/<int:id>')
def update(id):
    client = database_connect.connect(db_type=db_type)

    params = {}
    params['checked'] = request.json.get('checked')
    params['name'] = request.json.get('name')
    params['id'] = request.json.get('id')

    response = client.update_by_id(params, id)

    if response:
        return {}, 204
    return {}, 404

@app.delete('/<int:id>')
def delete(id):
    client = database_connect.connect(db_type=db_type)

    response = client.delete_by_id(id=id)
    if response:
        return {}, 204 # For a DELETE request: HTTP 200 or HTTP 204 should imply "resource deleted successfully".
    return {}, 404

# @app.get('/graphql')
# def graphql():
#     return 200

if __name__ == "__main__":
    app.run()
