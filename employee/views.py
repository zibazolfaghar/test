from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import employee
from.serializers import employeemodelserializer


@api_view(["POST"])
def post_employee(request):
    data={
        'name':request.data['name'],
        'age':request.data['age'],
        'salary':request.data['salary'],
        'post':request.data['post'],
        'name':request.data['name'],
        'name':request.data['name']



    }
    ser=employeemodelserializer(data=data)
    if ser.is_valid():
        ser.save()
        Response(ser.errors, status=status.HTTP_201_CREATED)
    else:
        Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)