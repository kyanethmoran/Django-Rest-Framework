from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    students = [
        {
            'id': 0, 'name': 'john doe', 'age': 12
        },
        {
            'id': 1, 'name': 'jane doe', 'age': 11
        },
    ]
    return HttpResponse(students)