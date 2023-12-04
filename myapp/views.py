from django.shortcuts import render
from rest_framework import generics
from .models import Empolyee
from .serializers import EmployeeSerializer
# Create your views here.

class Employeelist(generics.ListCreateAPIView):
	queryset=Empolyee.objects.all()
	serializer_class=EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Empolyee
	serializer_class=EmployeeSerializer
