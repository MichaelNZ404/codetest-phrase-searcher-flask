from flask import Flask, request, jsonify

from microservice.models import Glossary

app = Flask(__name__)
glossary = Glossary()

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/', methods=['GET'])
def index():
    searchword = request.args.get('text', '')
    if searchword == '':
        raise InvalidUsage('You need to provide a value for the parameter text', status_code=400)
    results = glossary.search(searchword)
    return jsonify(results)
