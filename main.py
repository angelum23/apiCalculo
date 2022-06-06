from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/montaGrafico', methods=['GET', 'POST'])
def monta_grafico():
    if request.method == 'GET':
        return jsonify({'response': 'Get request called'})
    elif request.method == 'POST':
        formula = str(request.args.get('formula'))
        list_results = list()
        for i in range(-10, 10):
            f1 = formula
            f1 = f1.replace('x²', str(i)+'*'+str(i))
            f1 = f1.replace('x', str(i))
            list_results.append(f1)
        return jsonify({'listFunc': list_results})


app.run(debug=True)
