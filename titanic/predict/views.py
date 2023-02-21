from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd


def predict(request):
    return render(request, 'predict.html')

def predict_changes(request):

    if request.POST.get('action') == 'post':
        Pclass = float(request.POST.get('Pclass'))
        Age = float(request.POST.get('Age'))
        Age_Sex = float(request.POST.get('Age_Sex'))

        model = pd.read_pickle(r"C:\Users\sellaway\PycharmProjects\titanic\titanic.pkl")
        result = model.predict([[1000,Pclass,Age,Age_Sex]])

        classification = result[0]

        return JsonResponse({'result': int(classification), 'Pclass': int(Pclass), 'Age':int(Age), 'Age_Sex':int(Age_Sex)},safe=False)

        #PredResults.objects.create(Pclass=Pclass, Age=Age, Age_Sex=Age_Sex, classification=classification)