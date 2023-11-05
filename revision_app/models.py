from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=60)
    admission_number = models.IntegerField()
    profile = models.ImageField(upload_to='students', default='profile.png')
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

# Create your models here.
