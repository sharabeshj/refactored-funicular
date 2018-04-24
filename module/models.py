from django.db import models
from hashid_field import HashidAutoField

# Create your models here.

class Project(models.Model):
	id = HashidAutoField(primary_key = True,min_length = 24,alphabet = "0123456789abcdefghijklmnopqrstuvwxyz")
	name = models.CharField(max_length = 40)

class Module(models.Model):
	id = HashidAutoField(primary_key = True,min_length = 24,alphabet = "0123456789abcdefghijklmnopqrstuvwxyz")
	name = models.CharField(max_length = 40)
	project = models.ForeignKey(Project,related_name = 'module',on_delete = models.CASCADE)

	