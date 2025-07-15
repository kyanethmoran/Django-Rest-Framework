# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
#for class based employee view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404


# Create your views here.
# def studentsView(request):
#     students = Student.objects.all()

    #this is just to help with debugging
    # print(students)

    #manually serialize the student data by converting it into a list (manual serialization is not recommended, can easily lead to overcomplication or errors)
    # students_list = list(students.values())

    #Serialize students with built-in option

    # return JsonResponse(students_list, safe=False)

#add a decorator to specify what methods you want studentsView to be able to perform
@api_view(['GET','POST'])
#define studentsView
def studentsView(request):
    #set request type to GET to receieve data
    if request.method =='GET':
        # Get all data from the Student table
        students = Student.objects.all()
        #use the serializer and use many to ensure all data is handled
        serializer = StudentSerializer(students, many=True)
        #return the response as well as the HTTP status 200
        return Response(serializer.data, status=status.HTTP_200_OK)
    #set request type to POST to save data
    elif request.method == 'POST':
        #serializer takes in request.data
        serializer = StudentSerializer(data=request.data)
        #check if data is valid
        if serializer.is_valid():
            #save if valid
            serializer.save()
            #return data and http created status
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #if data is invalid, return the errors and status of bad request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#get a single object primary key based operation
#This is for the function based views
@api_view(['GET','PUT', 'DELETE'])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        #we pass the current student data and the updated data from the request to the serializer
        serializer = StudentSerializer(student, data= request.data)
        if serializer.is_valid():
            #if valid save the serializer
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            #if not valid then show errors and that the request was bad
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#class based views for employees to get all employees and post an employee
class Employees(APIView):
    #create a member function for each http request
    def get(self, request):
        employees = Employee.objects.all()
        #import the employee serializer as well
        serializer = EmployeeSerializer(employees, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
#class for employeeDetail to get put delete specific employee detail individually
class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            #need to import Http404 from django
            raise Http404
    
    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

