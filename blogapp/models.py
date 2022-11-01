import email
from unicodedata import category
from click import password_option
from django.db import models
from datetime import datetime

# Create your models here.
class BlogAppUser(models.Model):
    first_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100,blank=True)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    contact=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    profile=models.FileField(upload_to='images',null=True)
    verification_code=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_verified=models.BooleanField(default=False)
    is_removed=models.BooleanField(default=False)
    created_at=models.DateTimeField(default=datetime.now())
    updated_at=models.DateTimeField(null=True)
    removed_at=models.DateTimeField(null=True)

    class Meta:
        db_table='dhurbapp_bloguser'

    def __str__(self):
        return self.first_name    

class BlogPost(models.Model):
    post_title=models.CharField(max_length=200)
    post_description=models.TextField(max_length=500)
    slug=models.CharField(max_length=200)
    category_id=models.BigIntegerField(null=True)
    post_image= models.FileField(upload_to='images/post/')
    user_id=models.BigIntegerField(null=True)
    post_status=models.CharField(null=True,max_length=20) 
    created_at=models.DateTimeField(default=datetime.now(),blank=False)
    updated_at=models.DateTimeField(null=True,blank=True)
    removed_at=models.DateTimeField(null=True,blank=True)

    class Meta:
        db_table="dhurbaapp_blogposts"
   

class BlogCategory(models.Model):
    category=models.CharField(max_length=100)
    parent_id=models.BigIntegerField(null=True)

    class Meta:
        db_table="app_blogcategories"

    def __str__(self):
        return self.category 
