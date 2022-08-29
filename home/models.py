from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=12,null=False)
    lastname = models.CharField(max_length=12,null=False)
    email = models.EmailField(max_length=20,null=False)


    def __str__(self):
        return self.firstname