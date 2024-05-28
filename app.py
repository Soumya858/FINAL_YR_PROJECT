from flask import Flask, render_template, request,redirect, url_for
import pickle
import numpy as np

app = Flask(__name__)

# Dictionary to store models
models = {
    'Decision Tree': pickle.load(open('./DecesionTree.pkl', 'rb')),
    'Bagg': pickle.load(open('./Bagg.pkl', 'rb')),
    'Random Forest': pickle.load(open('./RandomForest.pkl', 'rb')),
    'Logistic Regression': pickle.load(open('./LogisticRegression.pkl', 'rb')),
    # Add more models here as needed
}

@app.route('/')
def index():
    # Redirect to page2
    return render_template('patient.html')





# @app.route('/')
# def index():
#     return render_template('patient.html')

@app.route('/predict', methods=['POST'])
def predict_placement():
    # Get user choice of model
    # selected_model = request.form.get('model')
    
    # Load the selected model
    #model = models.get(selected_model)

    model1= list(models.values())[0]
    model2=list(models.values())[1]
    model3=list(models.values())[2]
    model4=list(models.values())[3]





    # if model is None:
    #     return render_template('index.html', error='Selected model not found.')

    # Get form data
    radius_mean = float(request.form.get('rm'))
    texture_mean = float(request.form.get('tm'))
    perimeter_mean = float(request.form.get('pm'))
    area_mean = float(request.form.get('am'))
    smoothness_mean = float(request.form.get('sm'))
    compactness_mean = float(request.form.get('comm'))
    concavity_mean = float(request.form.get('conm'))
    concave_points_mean = float(request.form.get('cpm'))
    symmetry_mean = float(request.form.get('symm'))
    fractal_dimension_mean = float(request.form.get('fdm'))

    # prediction
    

   
    data = np.array([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean]])
    result = model1.predict(data)
    #data1 = np.array([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean]])
    result1=model2.predict(data)
    result2=model2.predict(data)
    result3=model2.predict(data)

    show_div=True

    if result and result1 and result2 and result3 == ['B']:
        result = 'Benign'
        result1 = 'Bening'
        result2 = 'Benign'
        result3 = 'Benign'
    else:
        result = 'Malignant'
        result = 'Malignant'
        result1 = 'Malignant'
        result2 = 'Malignant'
        result3 = 'Malignant'    
    return render_template('patient.html', show_div=show_div, pred='The tumor is classified by Decision Tree Algorithm as {}'.format(result), pred1='The tumor is classified by Bagg Algorithm as {}'.format(result1), pred2='The tumor is classified by Random Forest Algorithm as {}'.format(result2))

   

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3434)
