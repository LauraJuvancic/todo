from __future__ import unicode_literals
from django.contrib.auth.models import User
from datetime import datetime

from django.db import models

# Create your models here.

class Tasks(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    category = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)
    alarm = models.BooleanField(default=False)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

class Home(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    info = models.TextField(blank=True)
    alarm = models.BooleanField()
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Work(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    info = models.TextField(blank=True)
    mails = models.EmailField(blank=True)
    workers = models.TextField(blank=True)
    alarm = models.BooleanField()
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Personal(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    info = models.TextField(blank=True)
    alarm = models.BooleanField()
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Travel(models.Model):
    name = models.CharField(max_length=50, help_text=None)
    departure = models.DateField(help_text=None)
    arrival = models.DateField(help_text=None)
    destination = models.CharField(max_length=100)
    pack = models.TextField(blank=True)
    info = models.TextField(blank=True)
    alarm = models.BooleanField()
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Shopping(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    stuff = models.TextField(blank=True)
    alarm = models.BooleanField()
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Birthday(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    presents = models.TextField(blank=True)
    alarm = models.BooleanField()
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Cooking(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    ingredients = models.TextField(blank=True)
    procedure = models.TextField(blank=True)
    alarm = models.BooleanField()
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
