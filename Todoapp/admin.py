from django.contrib import admin

# Register your models here.
from Todoapp.models import task

admin.site.register(task)