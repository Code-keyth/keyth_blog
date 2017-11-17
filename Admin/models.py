from django.db import models

# Create your models here.
import time
class Blog(models.Model):
    title = models.CharField(max_length=255)
    label = models.CharField(max_length=100)
    thumbnail = models.FileField(upload_to = './static/admin/upload/',null=True)
    autor = models.IntegerField()
    state = models.IntegerField(default=1)
    clicks = models.IntegerField(default=0)
    outline = models.TextField()
    editorValue = models.TextField()
    createtime = models.DateTimeField(default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    updatetime= models.DateTimeField(default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )

class Skill(models.Model):
    title = models.CharField(max_length=254)
    label = models.CharField(max_length=100)
    thumbnail = models.FileField(upload_to = './static/admin/upload/',null=True)
    autor = models.IntegerField()
    classify = models.IntegerField()
    state = models.IntegerField(default=1)
    clicks = models.IntegerField(default=0)
    outline = models.TextField()
    editorValue = models.TextField()
    createtime = models.DateTimeField(default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    updatetime= models.DateTimeField(default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )

class Users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    true_name = models.CharField(max_length=20,null=True)
    cookile = models.CharField(max_length=50,default='NULL')
    is_root = models.IntegerField(default=0)
    state = models.IntegerField(default=1)
    loginip = models.CharField(max_length=20,default='NULL')
    logintime = models.CharField(max_length=20,default='NULL')

class Skill_type(models.Model):
    name = models.CharField(max_length=30)
