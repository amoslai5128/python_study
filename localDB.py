from tinydb import TinyDB, Query

db = TinyDB('/Users/amoslai/Documents/GitHub/PY_Test/db.json', create_dirs=True)

query = Query()

def saveFormToDB(data):
    print('[ saveFormToDB ]: {form_data}')
    db.insert({'id': data['email'], 'result': data})

def queryFormResult(email):
    return db.search(query.id == email)