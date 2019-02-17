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
    req = json.loads(request.body)
    if req['command'] == "add":
        med = Medicine(name=req['name'], timeGap=(int)(req['time']))
        print(med.timeGap)
        print("HI")
        med.save()

    if req['command'] == "remove":
        Medicine.objects.filter(name=req['name']).delete()
    return HttpResponse("OK")

@csrf_exempt
def test(request):
    #Do your regular get method processes here
    if request.POST:
        print("HI")
        #Do something with post data here
    #return render('form.html', locals(), context_instance = RequestContext(request))
