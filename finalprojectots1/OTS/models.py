from django.db import models

class Question(models.Model):
     qno=models.IntegerField(primary_key=True,auto_created=True)
     que=models.CharField(max_length=200)
     optiona=models.CharField(max_length=100)
     optionb=models.CharField(max_length=100)
     optionc=models.FileField(upload_to="blog_image/",max_length=250,null=True,default=None)
     optiond=models.CharField(max_length=100)
     answer=models.CharField(max_length=1)
class User(models.Model):
     username=models.CharField(max_length=20,primary_key=True)  
     password=models.CharField(max_length=20)
     role=models.CharField(max_length=20)
     realname=models.CharField(max_length=20)