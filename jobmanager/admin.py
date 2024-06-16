from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models.aggregates import Count
from django.http import HttpRequest
from jobmanager.models import Author, JobPost,Location, Skills
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
    list_display = ["id","name","company","jobs_posted_count"]
    search_fields = ["name"]

    def jobs_posted_count(self,author):
        return author.jobpost_set.count()
    
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["id","city","state"]
    search_fields = ["city"]


@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


     