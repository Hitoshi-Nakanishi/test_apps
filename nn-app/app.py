from flask import Flask, render_template, request
import tensorflow as tf

app = Flask(__name__)

# Load your trained model here if you have one
# model = ... (Load your model as needed)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_value = float(request.form['inputValue'])
    # Here you can use the trained model to make predictions
    prediction = input_value ** 2  # Replace with model.predict(...) if you have a model
    return {'prediction': prediction}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)