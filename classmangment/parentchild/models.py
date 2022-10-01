from tkinter import CASCADE
from django.db import models

class parent(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)

class child(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    parent_id = models.ForeignKey(parent, on_delete=models.CASCADE)

class classes(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 100)
    seats  = models.IntegerField()

class enroll(models.Model):
    child_id = models.ForeignKey(child, on_delete=models.CASCADE)
    class_id = models.ForeignKey(classes, on_delete=models.CASCADE)