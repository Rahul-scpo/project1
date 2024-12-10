from django.contrib import admin
from app_13.models import logintable
from app_13.models import usertable
from app_13.models import  personaltable


# Register your models here.
admin.site.register(logintable)
admin.site.register(usertable)
admin.site.register(personaltable)
