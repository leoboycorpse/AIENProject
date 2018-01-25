from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=20,null=False)
    email = models.CharField(max_length=10,null=False)
    password = models.EmailField(max_length=100,blank=True)
    address = models.DateField(null=False)
    phone = models.DateField(null=False)
    
    class Meta:
        db_table = "members"