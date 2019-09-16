from flask import Flask, jsonify, request, render_template
import functools

app = Flask(__name__)

@app.route('/')
def home():
    test = {
        'hola': 'mundo',
        'foo':1,
        'bar':0
    }
    return jsonify(test)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
