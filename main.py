from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def montaGrafico():
    return jsonify({"Text": 'Hello World!',
                    "Text2": 'Hello World!'})

app.run(debug=True)
