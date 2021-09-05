import re
from flask import Flask, send_file
from sequence import gen_graph

VALID = re.compile(r'^[01:]+$')
LIMIT = 32

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return send_file('./index.html')

@app.route('/graph/', defaults={'sequence': ''})
@app.route('/graph/<sequence>')
def generate_graph(sequence):
    if VALID.search(sequence):
        bins = sequence.split(':')

        if any(map(lambda x: len(x) > LIMIT, bins)):
            return '<h1> Sequence too long! </h1>'

        output = gen_graph(*bins)
        return output
    else:
        return '<h2>Only binary digits and space is allowed</h2>'

