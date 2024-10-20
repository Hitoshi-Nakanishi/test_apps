from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load the pre-trained model
model = tf.keras.models.load_model('mnist_model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    image = np.array(data['image']).reshape(1, 28, 28, 1)  # Reshape to model's expected input
    prediction = np.argmax(model.predict(image), axis=-1)
    return jsonify({"prediction": int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
