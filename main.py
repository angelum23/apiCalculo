from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/montaGrafico', methods=['GET', 'POST'])
def monta_grafico():
    if request.method == 'GET':
        return jsonify({'response': 'Get request called'})
    elif request.method == 'POST':
        req_json = request.json
        formula = req_json['formula']
        return jsonify({'text': formula})


app.run(debug=True)
