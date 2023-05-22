#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import requests



def employee_list(request):
    # employees = Employee_Profiles.objects.all()
    # return render(request, 'employee_list.html', {'employees': employees})
    a=json.loads(request.body)
    b=a['id']
    Emp_Prof = Employee_Profiles.objects.get(pk=b)
    
    Name=str(Emp_Prof.First_Name)
    First_Name = str(Emp_Prof.First_Name)
    Last_Name = str(Emp_Prof.Last_Name)
    Email = str(Emp_Prof.Email)
    Phone = int(Emp_Prof.Phone)
    Dob = str(Emp_Prof.Dob)
    Blood_Group = str(Emp_Prof.Blood_Group)
    
    Emp_Prof.First_Name = First_Name
    Emp_Prof.Last_Name = Last_Name
    Emp_Prof.Email = Email
    Emp_Prof.Phone = Phone
    Emp_Prof.Dob = Dob
    Emp_Prof.Blood_Group = Blood_Group
    Name = Emp_Prof.add_name()
    
    Emp_Prof.save()
    resposne = {Name : True}
    return JsonResponse(resposne)


# from django.shortcuts import render
# from .models import *
# from django.http import JsonResponse
# import json
# import requests

# def employee_list(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         emp_id = data['id']
#         emp_profile = Employee_Profiles.objects.get(pk=emp_id)
        
#         # Retrieve data from the request
#         first_name = data.get('first_name', emp_profile.First_Name)
#         last_name = data.get('last_name', emp_profile.Last_Name)
#         email = data.get('email', emp_profile.Email)
#         phone = data.get('phone', emp_profile.Phone)
#         dob = data.get('dob', emp_profile.Dob)
#         blood_group = data.get('blood_group', emp_profile.Blood_Group)
        
#         # Update the employee profile
#         emp_profile.First_Name = first_name
#         emp_profile.Last_Name = last_name
#         emp_profile.Email = email
#         emp_profile.Phone = phone
#         emp_profile.Dob = dob
#         emp_profile.Blood_Group = blood_group
#         emp_profile.save()
        
#         response = {emp_profile.add_name(): True}
#         return JsonResponse(response)
#     else:
#         employees = Employee_Profiles.objects.all()
#         return render(request, 'employee_list.html', {'employees': employees})
