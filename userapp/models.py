from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    g=[('male','male'),('female','female'),('other','other')]

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=120)
    birth=models.DateField()
    gander=models.CharField(choices=g,max_length=20)
    pic=models.ImageField(upload_to='pic')

