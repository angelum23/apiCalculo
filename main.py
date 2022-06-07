from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/montaGrafico', methods=['GET', 'POST'])
def monta_grafico():
    if request.method == 'GET':
        return jsonify({'response': 'Get request called'})
    elif request.method == 'POST':
        formula = str(request).strip()
        slc = slice((formula.find('=') + 1), None)
        slicestr = formula[slc]
        slc = slice(None, formula.find("'"))
        slicestr = slicestr[slc]
        splitformula = slicestr.replace("%", " ")
        splitformat = list()
        for i in splitformula:
            try:
                splitformat.append(int(i))
            except:
                splitformat.append(str(i))
        return jsonify({"jonson": splitformat})

app.run(debug=True)
