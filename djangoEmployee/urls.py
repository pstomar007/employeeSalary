from django.contrib import admin
from django.urls import path
from . import EmployeeController 
urlpatterns = [
    path('employeeinterface/',EmployeeController.Action_EmployeeInterface),
    path('showresults/',EmployeeController.Action_ShowResult),
    path('employeeinterfacenext/',EmployeeController.Action_EmployeeInterfaceNext),
    path('nextshowresults/',EmployeeController.Action_ShowResultNext),
    path('loginpage/',EmployeeController.LoginInterface),
    path('checkpassword',EmployeeController.Checkpassword)
]

