# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Medicine
from django.db import models

import json

# Create your views here.
@csrf_exempt
def catchRequest(request):
    print(request.body)
    try:
        req = json.loads(request.body.decode('utf-8'))
        print("HI")
    except Exception as e:
        print(e)
    if req['command'] == "add":
        print("startfile")
        med = Medicine(name=req['name'], timeGap=(int)(req['time']))
        print("file")
        med.save()

    if req['command'] == "remove":
        print("view function called for removal")
        print(Medicine.objects.filter(name=req['name']))
        Medicine.objects.filter(name=req['name']).delete()
        print("view function done with removal")

    if req['command'] == "record":
        if req['status'] == 0:
            num_missed = Medicine.objects.filter(pk=req['id']).values_list('num_pill_missed', flat=True)[0]
            obj = Medicine.objects.filter(pk=req['id'])
            obj.update(num_pill_missed = num_missed + 1)
        if req['status'] == 1:
            num_taken = Medicine.objects.filter(pk=req['id']).values_list('num_pill_taken', flat=True)[0]
            obj = Medicine.objects.filter(pk=req['id'])
            obj.update(num_pill_taken = num_taken + 1)

    if req['command'] == "give_record":
        myfile = open("record.txt")
        for medicine in Medicine.objects.all():
            name = medicine
            num_pill_taken = medicine.values_list('num_pill_taken', flat=True)[0]
            num_pill_missed = medicine.values_list('num_pill_missed', flat=True)[0]
            myfile.write("{},{},{}".format(name, num_pill_taken + num_pill_missed, num_pill_taken))
            if (int)(req['delete']) == True:
                medicine.update(num_pill_taken = 0)
                medicine.update(num_pill_missed = 0)
    return HttpResponse("OK")

@csrf_exempt
def catchRecord(request):
    if request.POST:
        print("HI")

@csrf_exempt
def test(request):
    #Do your regular get method processes here
    if request.POST:
        print("HI")
        #Do something with post data here
    #return render('form.html', locals(), context_instance = RequestContext(request))
