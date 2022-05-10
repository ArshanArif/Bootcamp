from distutils.command.build_scripts import first_line_re
from django.db import models
from django.forms import CharField

# Create your models here.
class Regis(models.Model):
    fname=models.CharField(max_length=30,null=True)
    lname=models.CharField(max_length=30,null=True)
    Email=models.EmailField(max_length=30)
    Password=models.CharField(max_length=30)
    class Meta:
        db_table="Registration"
    

    