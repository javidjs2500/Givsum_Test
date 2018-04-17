from django.shortcuts import render
from .models import Organization, Event


# Create your views here.


def index(request):
    organizations = Organization.objects.all()
    return render(request, 'mainPage/index.html', 
    {'organizations': sorted(organizations, key = lambda x: x.name)
    })


def events(request):
    events = Event.objects.all()
    return render(request, 'mainPage/events.html',{'events': sorted(events,key = lambda x: x.name)}
    )
