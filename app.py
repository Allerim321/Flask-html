from flask import Flask, render_template
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)

@app.route('/')
def homepage():
        return render_template('home.html')

@app.route('/lista')
def lista():
    with open('text.csv', 'r') as file:
            reader = csv.DictReader(file)
            itens = list(reader)

    return render_template('index.html', itens=itens)

if __name__ == "__main__":
        app.run(debug=True, host="0.0.0.0")