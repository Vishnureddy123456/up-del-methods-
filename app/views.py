from django.shortcuts import render
from app.models import *
from django.db.models import Q
# Create your views here.
def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topics.html',d)
def display_webpages(request):
    webpages=Webpage.objects.all()
    #webpages=Webpage.objects.all()[::]
    #webpages=Webpage.objects.all()[::-1]
    #webpages=Webpage.objects.all().order_by('name')
    #webpages=Webpage.objects.all().order_by('-name')

    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)
def display_accessrecords(request):
    accessrecords=AccessRecord.objects.all()
    accessrecords=AccessRecord.objects.filter(date__gt='2021-06-16')
    accessrecords=AccessRecord.objects.filter(date__gte='2021-06-16')
    accessrecords=AccessRecord.objects.filter(date__lt='2021-06-16')
    accessrecords=AccessRecord.objects.filter(date__lte='2021-06-16')
    accessrecords=AccessRecord.objects.filter(date__year__gt='2021')
    accessrecords=AccessRecord.objects.filter(date__year__gte='2021')
    accessrecords=AccessRecord.objects.filter(date__year__lt='2021')
    accessrecords=AccessRecord.objects.filter(date__year__lte='2021')
    accessrecords=AccessRecord.objects.all()
    accessrecords=AccessRecord.objects.filter(name__in=[1,2])
    accessrecords=AccessRecord.objects.filter(id__in=[1,2])
    accessrecords=AccessRecord.objects.filter(Q(id=2)|Q(id=3))
    
    
    d={'accessrecords':accessrecords}
    return render(request,'display_accessrecords.html',d)
def update_webpages(request):
    Webpage.objects.filter(name='dhoni').update(topic_name='valleyball')
    Webpage.objects.filter(name='dhoni').update(topic_name='valleyball',url='https://cric.com')
    Webpage.objects.filter(name='naveen').update(topic_name='valleyball')
    Webpage.objects.update_or_create(name='dhoni',defaults={'url':'https://dhoni.com'})
    co=Topic.objects.get(topic_name='cricket')
    Webpage.objects.update_or_create(name='dhoni',defaults={'topic_name':co})
    webpages=Webpage.objects.all()

    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)
