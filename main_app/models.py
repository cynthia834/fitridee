from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=100)
    id_no = models.IntegerField(max_length=50)
    phone_number = models.CharField(max_length=15)
    groups = models.ManyToManyField(Group,related_name='customuser_set')  # Set a unique related_name
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions') # Set a unique

class Bicycle(models.Model):
    serial_number = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=50)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    station = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time_taken = models.DurationField()
    timer = models.DurationField()
    image = models.ImageField(upload_to='bicycles/', null=True, blank=True)

    def __str__(self):
        return f'{self.serial_number} - {self.color}'

