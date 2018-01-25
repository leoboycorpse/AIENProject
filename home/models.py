from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=45,null=False)
    email = models.CharField(max_length=100,null=False)
    password = models.EmailField(max_length=45,blank=True)
    address = models.CharField(max_length=100,null=False)
    phone = models.CharField(max_length=15,null=False)
    
    class Meta:
        db_table = "carmember"