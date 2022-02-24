from django.http import HttpResponse
from django.shortcuts import render
from .models import Coach, Student

# Create your views here.
def homePage(request):
    return HttpResponse("<h1>Welcome to the ...</h1> ")

def student_list(request):
    Studentslist = Student.objects.all()
   

    return render(
        request,
        'hub/index.html',
        {
            'Users': Studentslist,
        }
    )

def coach_list(request):
    Coachslist = Coach.objects.all()
   
    return render(
        request,
        'hub/index.html',
        {
            'Users': Coachslist,
        }
    )

def student_details(request, id): 
    student = Student.objects.get(pk=id)
    return render (
        request,
        'hub/us_details.html',
        {
            'User': student,
        }
    )
 