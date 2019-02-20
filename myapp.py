import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Names</h1>
<p>A prototype API for distant reading of Names.</p>'''


@app.route('/api/v1/resources/names/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('names.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_names = cur.execute('SELECT * FROM names;').fetchall()

    return jsonify(all_names)



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/names', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    name = query_parameters.get('name')


    query = "SELECT * FROM names WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if name:
        query += ' name=? AND'
        to_filter.append(name)
    if not (id or name):
        return page_not_found(404)


    query = query[:-3] + ';'

    conn = sqlite3.connect('names.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()
