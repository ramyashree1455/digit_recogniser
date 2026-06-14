# Digit Recognizer

A handwritten digit recognition web app using Deep Learning.

## What it does
- Draw a digit (0-9) on the canvas
- Click Predict
- The model tells you what digit you drew!

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- ML Model: TensorFlow/Keras
- Dataset: MNIST (Kaggle)

## How to run locally

1. Clone the repo
2. Install dependencies: pip install -r requirements.txt
3. Download train.csv from Kaggle and run Untitled.ipynb to generate the model
4. Run: python app.py
5. Open browser: http://localhost:5000

## Note
digit_model.keras and train.csv are not included due to file size limits.
Train the model using the notebook provided.