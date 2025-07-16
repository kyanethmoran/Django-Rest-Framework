from django.urls import path, include
from . import views
#import defaultRouter for working with viewsets
from rest_framework.routers import DefaultRouter


#for working with viewsets we need routers
router = DefaultRouter
router.register('employees', views.EmployeeViewset)

urlpatterns = [
    #student model paths (as a function based view)
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),

    
    #employee model paths (as a class based view)
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view())

    #for working with viewsets we need routers
    path('', include(router.urls))
]