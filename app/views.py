from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

def Insert_Topic(request):
    tn=input('Enter Topic name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic insert Successfully')

def display_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topic.html',context=d)

def Insert_Webpage(request):
    tn=input('Enter Topic name: ')
    na=input('Enter Name: ')
    ur=input('enter URL: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
    WO.save()
    return HttpResponse('Webpage inserted Successfully')

def display_webpage(request):
    LOW=Webpage.objects.all()
    d={'webpage':LOW}
    return render(request,'display_webpage.html',context=d)


def Insert_AccessRecords(request):
    tn=input('Enter Topic name: ')
    na=input('Enter Name: ')
    ur=input('enter URL: ')
    au=input('Enter Author name: ')
    da=input('Enter Date: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
    WO.save()
    AO=AccessRecords.objects.get_or_create(name=WO,author=au,date=da)[0]
    AO.save()
    return HttpResponse('Accessrecords inserted Successfully')

def display_accessrecords(request):
    LOA=AccessRecords.objects.all()
    d={'access':LOA}
    return render(request,'display_accessrecords.html',context=d)