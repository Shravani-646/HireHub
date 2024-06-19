from typing import Iterable
from django.db import models
from django.utils.text import slugify
from django.conf import settings

class Author(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    company = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    
class Skills(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name 
# Create your models here.
class JobPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True,blank=True,max_length=40)
    description = models.CharField(max_length=255)
    skills = models.ManyToManyField(to=Skills)
    location = models.ForeignKey(to='Location',on_delete=models.CASCADE,null=True)
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


class JobApplication(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    job_post = models.ForeignKey(to=JobPost,on_delete=models.CASCADE,related_name="applications")
    education = models.TextField()
    skills = models.ManyToManyField(to=Skills)
    available_to_start = models.DateField(null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    resume = models.FileField(upload_to="jobmanager/applications")
    
    

