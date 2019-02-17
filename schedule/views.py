# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Medicine, Client
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
    if req['command'] == "add": #fix
        print("startfile")
        med = Medicine(name=req['name'], timeGap=int(req['time']), user_id=int(req['user_id']))
        print("file")
        med.save()

    if req['command'] == "remove": #fix
        print("view function called for removal")
        print(Medicine.objects.filter(name=req['name']).filter(user_id=int(req['user_id'])))
        Medicine.objects.filter(name=req['name']).filter(user_id=int(req['user_id'])).delete()
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
        print("called give_record views function")
        
        for client in Client.objects.all():
            #print(dir(client))
            #print("client called: " + client)
            try:
                #print("record_{}.txt".format(client.phone))
                myfile = open("./record_{}.txt".format(client.phone), "w")
                print(client.pk)
                #myfile = open("hello", "w")
            except Exception as e:
                print('exception: '+str(e))
            for medicine in Medicine.objects.all():
                if client.pk == medicine.user_id:
                    try:
                        name = medicine.name.split(' ')[2]
                        num_pill_taken = medicine.num_pill_taken
                        num_pill_missed = medicine.num_pill_missed
                        print(name)
                        myfile.write("{},{},{},".format(name, num_pill_taken + num_pill_missed, num_pill_taken))
                        myfile.close()
                    except Exception as e:
                        print('exception: '+str(e))
                if int(req['delete']) == True:
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
