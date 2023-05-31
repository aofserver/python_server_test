import json
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/')
def hello():
    return "<h1> TEST API. </h1>" ,200

@app.route('/<file>', methods=['GET', 'POST'])
def test_api(file):
    f = open(f'route/{file}.json')
    data = json.load(f)
    return data,200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

