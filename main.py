from flask import Flask, request, jsonify

app = Flask(__name__)

def converteformula(request):
    request_strip = str(request).strip()
    slc = slice((request_strip.find('=') + 1), None)
    slice_str = request_strip[slc]
    slc = slice(None, slice_str.find("'"))
    slice_str = slice_str[slc]
    formula = slice_str.replace("%20", " ")
    formula = formula.replace("%2F", "/")
    return formula

@app.route('/montaGrafico', methods=['GET', 'POST'])
def monta_grafico():
    listax = list()
    listay = list()

    if request.method == 'GET':
        return jsonify({'response': 'Get request called'})
    elif request.method == 'POST':

        formula = converteformula(request)

        for i in range(-10, 10):
            formulaTemp = formula.replace("x²", str(i * i))
            formulaTemp = formulaTemp.replace("x", str(i))
            try:
                resultado = eval(formulaTemp)
            except:
                return 'Erro'
            listax.append(i)
            listay.append(resultado)

        return jsonify({'x': listax, 'y': listay})


app.run(debug=True)
