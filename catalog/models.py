from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    ID = models.AutoField(primary_key=True, unique=True)
    firstname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthday = models.DateTimeField(blank=True, null=True)
    school = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def add_student(self):
        #new = Student(firstname=firstname, )
        #self.save()
        pass

    def get_student(selfself, id):
        # return
        pass

    def add(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.firstname