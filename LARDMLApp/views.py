from .models import PredictionResult
from django.shortcuts import render
import joblib
import pandas as pd

# Create your views here.



def Predict(request):
    if request.method == 'POST':
        # Get the input data from the request
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        # Preprocess the input data as required by the model
        # processed_data = preprocess(input_data)

        # Load the trained model from the joblib file
        model = joblib.load('music-recommender.joblib')
        # Make predictions using the loaded model
        prediction = model.predict([[age, gender],])

        # Store the prediction result in your Django database
        result = PredictionResult(name=name, age=age, gender=gender, prediction=prediction)
        result.save()

        # Render the result template with the prediction result
        return render(request, 'resultml.html', {'prediction': prediction})
    else:
        # Render the form template for user input
        return render(request, 'formml.html')


# def FormML(request):
#     return render(request, 'formml.html')


# def ResultML(request):
#     return render(request, 'resultml.html')
