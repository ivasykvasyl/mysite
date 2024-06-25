from django.db import models
from django.urls import reverse

# Create your models here.
class DaysOfTheWeek(models.Model):
    day = models.CharField(max_length=64)

    def __str__(self):
        return self.day

class Discipline(models.Model):
    discipline = models.CharField(max_length=64)
    learning = models.ManyToManyField(DaysOfTheWeek, blank=True, related_name="disc")

    def __str__(self):
        return self.discipline

class Time(models.Model):
    time = models.CharField(max_length=64)
    learn = models.ManyToManyField(DaysOfTheWeek, blank=True, related_name="time")

    def __str__(self):
        return self.time

class Vykladach(models.Model):
    vykladach = models.CharField(max_length=64)
    learn1 = models.ManyToManyField(DaysOfTheWeek, blank=True, related_name="vykladach")

    def __str__(self):
        return self.vykladach

class Group(models.Model):
    group = models.CharField(max_length=64)
    learn2 = models.ManyToManyField(DaysOfTheWeek, blank=True, related_name="group")

    def __str__(self):
        return self.group
    
class Classroom(models.Model):
    classroom = models.CharField(max_length=64)
    learn3 = models.ManyToManyField(DaysOfTheWeek, blank=True, related_name="classroom")

    def __str__(self):
        return self.classroom
