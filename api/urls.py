from django.urls import path
from . import views

urlpatterns = [
    #student model paths (as a function based view)
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),

    #employee model paths (as a class based view)
    path('employees/', views.Employees.as_view())
]