
from flask import Flask, request, jsonify, render_template
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

#load full model directly - no rebuilding needed!
model = load_model('digit_model.keras')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json.get('image')
        if data is None:
            return jsonify({'error': 'no image provided'}), 400

        arr = np.array(data, dtype=np.float32).reshape(1, 28, 28) / 255.0
        print('max:', arr.max(), 'mean:', arr.mean())

        prediction = model.predict(arr)
        digit = int(np.argmax(prediction))

        return jsonify({
            'digit': digit,
            'stats': {'min': float(arr.min()), 'max': float(arr.max())}
        })
    except Exception as e:
        print('Error:', e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)