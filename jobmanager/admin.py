from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models.aggregates import Count
from django.http import HttpRequest
from jobmanager.models import Author, JobApplication, JobPost,Location, Skills
# Register your models here.

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
     autocomplete_fields = ["location","skills","author"]
     list_display = ["id","title","date","company"]
     list_per_page = 10
     list_filter = ["date","title","application_deadline"]
     ordering = ["id"]
     search_help_text = "Write your query and hit enter."
     search_fields = ["title__icontains"]
     list_select_related = ["author"]
     fieldsets = (
          ('Job Details',{
               'fields':('title','description','author')
          }),
          ('Additional Information',{
               'classes':("collapse",),
               'fields':("skills",'location','salary',"application_deadline")
          })
     )
     @admin.display(ordering="author__company")
     def company(self,jobpost):
        return jobpost.author.company
     
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id","fullname","company","jobs_posted_count"]
    search_fields = ["name"]
    autocomplete_fields = ["user"]

    def jobs_posted_count(self,author):
        return author.jobpost_set.count()
    
    def fullname(self,author):
        return f'{author.user.first_name} {author.user.last_name}'
    
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["id","city","state"]
    search_fields = ["city"]


@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    autocomplete_fields = ["user","job_post","skills"]
    list_display = ["id","job_post","user"]


     