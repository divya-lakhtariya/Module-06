from rest_framework import serializers
from .models import Empolyee

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model=Empolyee
		fields=('id','empolyee_name','department_id','department_name','salary')

 