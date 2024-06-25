from django.contrib import admin

from .models import DaysOfTheWeek, Discipline, Time, Vykladach, Group, Classroom
# Register your models here.
admin.site.register(DaysOfTheWeek)
admin.site.register(Discipline)
admin.site.register(Time)
admin.site.register(Vykladach)
admin.site.register(Group)
admin.site.register(Classroom)
