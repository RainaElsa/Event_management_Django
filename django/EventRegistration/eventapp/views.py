from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from .forms import Eventform

# Create your views here.


def index(request):
    events=Event.objects.all()
    context={'events':events}
    return render(request,'index.html',context)

def eventdetail(request,pk):
    events=Event.objects.get(pk=pk)
    if request.method == "POST":
        print("I got a post request from the frontend")
        form=Eventform(request.POST)
        if form.is_valid():
            fillform= form.save(commit=False)
            fillform.event=events
            fillform.save()

    form=Eventform()
    context={'event':events,'form':form}
    return render(request,'details.html',context)
    
