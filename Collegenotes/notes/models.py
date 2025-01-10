from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Signupinfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    studentclass = models.CharField(max_length=30)
    studentcollege = models.CharField(max_length=50)
    confpassword = models.CharField(max_length=10, default=0)

    def __str__(self):
        return self.user.username + self.user.first_name + self.user.last_name


class Uploadnotes(models.Model):
    teacher = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    dateofupload = models.DateField()
    file = models.FileField()

    def __str__(self):
        return str(self.subject) + '\t' + str(self.teacher)
