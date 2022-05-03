from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd


def get_num_of_patients(request):
    diabetes = request.GET.get("diabetes")
    if diabetes:
        csv_data = pd.read_csv('PimaIndiansDiabetes.csv')
        if 'diabetes' in csv_data.columns and diabetes == 'pos':
            result = csv_data[(csv_data['diabetes']) == diabetes]
            pos_diabetes_patients = len(result)
            avg_patients = round(sum(result['age'])/len(result)) if pos_diabetes_patients else 0
            return render(request,"index.html",{'get_num_of_patients':'num_patient','pos_diabetes':pos_diabetes_patients,'avg_patients':avg_patients})
        else:
            return HttpResponse('Invalid url request')
    else:
        return HttpResponse('Invalid url request')

def patients_with_age(request):
    diabetes = request.GET.get("diabetes")
    age = request.GET.get("age")
    if diabetes and age:
        csv_data = pd.read_csv('PimaIndiansDiabetes.csv')
        if 'diabetes' and 'age' in csv_data.columns and diabetes == 'pos':
            result = csv_data[(csv_data['diabetes'] == diabetes ) & (csv_data['age'] == int(age))]
            patients_with_age_and_pos = len(result)
            return render(request,"index.html",{'patients_with_age':'patients_with_age','patients_with_age_and_pos':patients_with_age_and_pos})
        else:
            return HttpResponse('Invalid url request')
    else:
        return HttpResponse('Invalid url request')

def patients_list(request):
    diabetes = request.GET.get("diabetes")
    age = request.GET.get("age")
    if diabetes and age:
        csv_data = pd.read_csv('PimaIndiansDiabetes.csv')
        if 'diabetes' and 'age' in csv_data.columns and diabetes == 'pos' and int(age) == 55 :
            result = csv_data[(csv_data['diabetes'] == diabetes) & (csv_data['age'] == int(age))]
            data_to_send = result.to_dict('records')
            return render(request, "index.html", {'patients_list': 'patients_list',
                                                  'data': data_to_send})
        else:
            return HttpResponse('Invalid url request')
    else:
        return HttpResponse('Invalid url request')
