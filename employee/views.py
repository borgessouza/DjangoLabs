# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from employee.models import Employee
from employee.serializers import employee_serializer

# Create your views here.
@csrf_exempt
def employee_list(request):
    """
    Get all employee from db and return in json format
    Post (save) a new employee in the database
    """
    if request.method == 'GET':
        #Get all object form database
        employee = Employee.objects.all()
        #Serializer all
        serializer = employee_serializer(employee, many=True)
        #return to the request
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        #retrive the post content
        data = JSONParser().parse(request)
        # Serializer it
        serializer = employee_serializer(data=data)
        if serializer.is_valid():
            # if is correct, save in the database
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        #otherside return an error (400)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def employee_detail(request, pk):
    """
    Get details, update or delete a specific (pk) employee
    """
    try:
        #Find employee by the id
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        #if not exist!!
        return HttpResponse(status=404)

    #if the request is get
    if request.method == 'GET':
        #return the employee in Json
        serializer = employee_serializer(employee)
        return JsonResponse(serializer.data)

    #if request is put
    elif request.method == 'PUT':
        #parse the body request content
        data = JSONParser().parse(request)
        #Serializer the employee
        serializer = employee_serializer(employee, data=data)
        if serializer.is_valid():
            #save if is valid
            serializer.save()
            return JsonResponse(serializer.data)
        #otherside return 400 - bad Request
        return JsonResponse(serializer.errors, status=400)

    #if request is delete
    elif request.method == 'DELETE':
        #end of live of the employee
        employee.delete()
        #return No content
        return HttpResponse(status=204)