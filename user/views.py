from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from user.models import Patient, Details

import json
import cv2
import numpy as np
import base64 
import time
from pyzbar.pyzbar import decode
from PIL import Image
import os

import urllib
import re

import xmltodict
import pprint
import csv 
import xml.etree.ElementTree as ET
# Create your views here.


@login_required
def dashboard(request):
    return render(request, 'user/dashboard.html',{'title':'Dashboard'})

def data_uri_to_cv2_img(uri):
    # encoded_data = uri.split(',')[1]
    # print(encoded_data[:20])
    encoded_data = uri
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    print(img)
    return img

def newPatient(request):
    if request.method =="POST":
        get_value = str(request.body)
        get_value = urllib.parse.unquote(get_value)
        get_value = get_value[8:]
        get_value = get_value[:-86]
        # print(get_value[-5:])

        file = open("testfile.txt","w")
        file.write(get_value)
        file.close()

        # Do your logic here coz you got data in `get_value`
        data = {}
        inputImage = data_uri_to_cv2_img(get_value)
        # print(type(inputImage))
        #img=open("img.jpg","w")
        cv2.imwrite("img.jpg",inputImage)
        #img.close()

        qrDecoder = cv2.QRCodeDetector()
        message,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)
        decoded=decode(cv2.imread('img.jpg'))
      
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(json.dumps(xmltodict.parse(message)))
        # print(message["PrintLetterBarcodeData"].)

        if len(message) or len(decoded) > 0:
            message = decoded[0].data
            message = str(message)
            #message = message.strip()
            print(type(message))
            message = message[2:]
            message = message[:-1]
            print(message)
            #message[38:40]=" "

            data['result'] = message
        else:
            data['result'] = 'Could not Detect QR Code'
        # Detect and decode the qrcode
        t = time.time()
        # xmlfile=open('xmlfile.xml','wb')
        # xmlfile.write(message)


        #-------------------------------------------------------------------
        #Implementation 
        #Parsing and Pushing the XML data into Database
        parsedxml=xmltodict.parse(data['result'])
        print(f"Name: {parsedxml['PrintLetterBarcodeData']['@name']}")

        #-------------------------------------------------------------------

        return HttpResponse(json.dumps(data), content_type="application/json")
    elif request.method == 'GET':
        return render(request, 'user/newPatient.html')





def about(request):
    return render(request, 'user/about.html')


@login_required
def profile(request):
    return render(request, 'user/profile.html')


class DoctorsList(ListView):
    model = Details
    template_name = 'user/doctors.html'
    context_object_name = 'details'


class PatientList(ListView):
    model = Patient
    template_name = 'user/patients.html'
    context_object_name = 'patients'


class HistoryList(ListView):
    model = Details
    template_name = 'user/history.html'
    context_object_name = 'details'
    context = {'patients': Patient}


def report(request):
    patients=Patient.objects.all().values()
    details=Details.objects.all().values()
    return render(request,'user/report.html',{'patients': patients,'details': details})
