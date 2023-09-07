from django.contrib import admin
from userapp.models import Profile
# Register your models here.


class ok(admin.ModelAdmin):
    list_display=('id','status','birth','gander','pic')
admin.site.register(Profile,ok)