from django.shortcuts import render
from django.views.generic import TemplateView
from .models import DaysOfTheWeek, Discipline, Time, Vykladach, Group, Classroom
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "schedule/index.html", {
        "schedule": DaysOfTheWeek.objects.all()
    })

def sch(request, sch_id):
    sch = DaysOfTheWeek.objects.get(pk=sch_id)
    return render(request, "schedule/day.html", {
        "sch": sch,
        "disc": sch.disc.all(),
        "non_disc": Discipline.objects.exclude(learning=sch).all,
        "time": sch.time.all(),
        "non_time": Time.objects.exclude(learn=sch).all,
        "vykladach": sch.vykladach.all(),
        "non_vykladach": Vykladach.objects.exclude(learn1=sch).all,
        "group": sch.group.all(),
        "non_group": Group.objects.exclude(learn2=sch).all,
        "classroom": sch.classroom.all(),
        "non_classroom": Classroom.objects.exclude(learn3=sch).all
        
    })

def add(request, sch_id):
    if request.method == "POST":
        sch = DaysOfTheWeek.objects.get(pk=sch_id)
        disc = Discipline.objects.get(pk=int(request.POST["disc"]))
        disc.learning.add(sch)
        time = Time.objects.get(pk=int(request.POST["time"]))
        time.learn.add(sch)
        vykladach = Vykladach.objects.get(pk=int(request.POST["vykladach"]))
        vykladach.learn1.add(sch)
        group = Group.objects.get(pk=int(request.POST["group"]))
        group.learn2.add(sch)
        classroom = Classroom.objects.get(pk=int(request.POST["classroom"]))
        classroom.learn3.add(sch)
        return HttpResponseRedirect(reverse("day", args=(sch.id,)))