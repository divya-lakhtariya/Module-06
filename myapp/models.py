from django.db import models

# Create your models here.
class Empolyee(models.Model):
	empolyee_name=models.CharField(max_length=100,blank=True)
	department_id=models.PositiveIntegerField(blank=True)
	department_name=models.CharField(max_length=100,blank=True)
	salary=models.PositiveIntegerField(blank=True)

	def __str__(self):
		return self.empolyee_name

