from flask import Flask, send_file, Response

from sequence import gen_graph

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return send_file('./index.html')

@app.route('/graph/<sequence>')
def generate_graph(sequence):
    bins = sequence.split(':')
    output = gen_graph(*bins)
    return Response(output, mimetype='text/svg')
