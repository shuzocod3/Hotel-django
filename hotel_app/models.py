from django.db import models

from django.contrib.auth.models import AbstractUser

from django.conf import settings


class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    cost = models.IntegerField(null=True)
    description = models.TextField()

    def __str__(self):
        return f"Room #{self.number}"


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f"{self.room} - {self.creation_time}"


class Employee(models.Model):
    name = models.CharField(max_length=17)
    age = models.IntegerField()
    work = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} - {self.work}"