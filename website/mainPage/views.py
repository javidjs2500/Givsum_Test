from django.shortcuts import render
from .models import Organization, Event


# Create your views here.


def index(request):
    if request.method == 'POST':
        event = Event()
        event.name = request.POST.get('name')
        event.time = request.POST.get('time')
        event.date = request.POST.get('date')
        event.event_description = request.POST.get('event_description')
        event.address = request.POST.get('address')
        event.picture_url = request.POST.get('picture_url')
        if request.POST.get('picture_url') == '':
            event.picture_url = 'http://via.placeholder.com/120x120'
        event.save()
    organizations = Organization.objects.all()
    return render(request, 'mainPage/index.html', 
    {'organizations': sorted(organizations, key = lambda x: x.name)
    })


def events(request):
    events = Event.objects.all()
    return render(request, 'mainPage/events.html',{'events': sorted(events,key = lambda x: x.name)}
    )
