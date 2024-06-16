from typing import Iterable
from django.db import models
from django.utils.text import slugify
from django.contrib import admin

class Author(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
class Skills(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name 
# Create your models here.
class JobPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True,blank=True,max_length=40,unique=True)
    description = models.CharField(max_length=255)
    skills = models.ManyToManyField(to=Skills)
    location = models.OneToOneField(to='Location',on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()
    application_deadline = models.DateField(null=True,blank=True)
    author = models.ForeignKey(to=Author,on_delete=models.CASCADE,null=True)


    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.id:
            base_slug = slugify(self.title)
            unique_suffix = self.author.company
            self.slug = f"{base_slug}-{slugify(unique_suffix)}-{slugify(self.location.city)}"
        return super().save(*args, **kwargs)  
    

class Location(models.Model):
    #street,city,state,country,zipcode
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.city} - {self.state}'
    
    

