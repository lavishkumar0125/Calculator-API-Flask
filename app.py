from flask import Flask,render_template,request,jsonify
from basicCalculator import basic_calculator

app = Flask(__name__)
PORT = 4000

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    a = request.form['a']
    b = request.form['b']
    operation = str(request.form['operation'])
    result = basic_calculator(a,b, operation)
    return render_template('index.html', prediction_text = str(result))

if __name__ == '__main__':
    app.run(port = PORT,debug=True)