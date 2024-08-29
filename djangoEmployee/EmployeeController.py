from django.shortcuts import render

def Action_EmployeeInterface(request):
    return render(request, "Employee.html", {'show': False})
def Action_EmployeeInterfaceNext(request):
    return render(request, "nextEmployee.html",{'show':False})

def Action_ShowResult(request):
    employeeId = request.GET['empId']
    employeeName = request.GET['empName']
    gender = request.GET['gender']
    designation = request.GET['designation']
    salary = int(request.GET['salary'])

    if gender == "Male":
        prefix = 'mr'
    else:
        prefix = 'mrs'

    if designation == "Grade One":
        da = 70
        hra = 16
        pf = 12
    elif designation == "Grade Two":
        da = 50
        hra = 16
        pf = 12
    elif designation == "Grade Three":
        da = 30
        hra = 10
        pf = 12

    daamt = salary * da / 100
    hraamt = salary * hra / 100
    pfamt = salary * pf / 100
    netsalary = salary + daamt + hraamt + pfamt

    return render(request, 'Employee.html', {
        'prefix': prefix,
        'employeeId': employeeId,
        'employeeName': employeeName,
        'gender': gender,
        'designation': designation,
        'salary': salary,
        'da': da,
        'hra': hra,
        'pf': pf,
        'daamt': daamt,
        'hraamt': hraamt,
        'pfamt': pfamt,
        'netsalary': netsalary,
        'show': True
    })


def Action_ShowResultNext(request):
    employeeId = request.GET['empId']
    employeeName = request.GET['empName']
    gender = request.GET['gender']
    designation = request.GET['designation']
    salary = int(request.GET['salary'])

    if gender == "Male":
        prefix = 'mr'
    else:
        prefix = 'mrs'

    if designation == "Grade One":
        da = 70
        hra = 16
        pf = 12
    elif designation == "Grade Two":
        da = 50
        hra = 16
        pf = 12
    elif designation == "Grade Three":
        da = 30
        hra = 10
        pf = 12

    daamt = salary * da / 100
    hraamt = salary * hra / 100
    pfamt = salary * pf / 100
    netsalary = salary + daamt + hraamt + pfamt

    return render(request, 'ShowEmployeePayslip.html', {
        'prefix': prefix,
        'employeeId': employeeId,
        'employeeName': employeeName,
        'gender': gender,
        'designation': designation,
        'salary': salary,
        'da': da,
        'hra': hra,
        'pf': pf,
        'daamt': daamt,
        'hraamt': hraamt,
        'pfamt': pfamt,
        'netsalary': netsalary
    })

def LoginInterface(request):
    return render(request,'LoginPage.html',{'message':''})
def Checkpassword(request):
    userid=request.POST['userid']
    password=request.POST['password']
    if(userid=='india' and password=='india'):
        return render(request,"NextEmployee.html")
    else:
        return render(request,"LoginPage.html",{'message':'Invaild userid/password'})


