# CRUD

## CREATE
- `curl -i -XPOST 'http://127.0.0.1:5000/' -H "Content-Type: application/json" -d '{"name": "teste"}'`

## READ
- `curl -i -XGET 'http://127.0.0.1:5000/'`
- OBS: Could be accessed by browser.

## UPDATE
- `curl -i -XPUT 'http://127.0.0.1:5000/1' -H "Content-Type: application/json" -d '{"checked": true}'`
- `curl -i -XPUT 'http://127.0.0.1:5000/1' -H "Content-Type: application/json" -d '{"name": "new Task"}'`
- `curl -i -XPUT 'http://127.0.0.1:5000/1' -H "Content-Type: application/json" -d '{"checked": true, "name": "new Task"}'`

## DELETE
- `curl -i -XDELETE 'http://127.0.0.1:5000/1' -H "Content-Type: application/json"`