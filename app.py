from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def homepage():
        return render_template('home.html')

@app.route('/produtos')
def produtos():
        with open('Text.csv', 'r') as file:
                reader = csv.DictReader(file)
                itens = list(reader)

        return render_template('produtos.html', itens=itens)

if __name__ == "__main__":
        app.run(debug=True, host="0.0.0.0")