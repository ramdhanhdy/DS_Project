from flask import Flask, render_template, request
from catboost import CatBoostRegressor

app = Flask(__name__)

# Load the model
model = CatBoostRegressor()
model.load_model('D:\\CDS590\\src\\models\\best_catboost_model.cbm')

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Add prediction logic here
#     data = request.form
#     # Process data and make prediction
#     prediction = model.predict([list(data.values())])
#     return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)