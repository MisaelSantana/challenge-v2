"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse, HttpResponse
from app.models import data
from django.db import connection

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Challenge',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def apiTeste(request):
    from app.apiV1Teste.testes import Alive
    return JsonResponse(Alive().makeAliveObject())

def apiState(request):
    from app.apiV1Teste.testes import State
    if request.GET == {}:
        return HttpResponseBadRequest(State().makeAliveObject(ApplicationStatus = 0, HTTPStatus = 400, errorTitle = 'Erro de Bad Request', errorMessage = {}), content_type='application/json')
    return HttpResponse(State().makeAliveObject(requestGetData = request.GET), content_type='application/json')

def apiTesteResponse(response):
    from app.apiV1Teste.testes import AliveResponse
    if response.GET == {}:
        return HttpResponse(AliveResponse().AliveResponseObject(), content_type='application/json')
    return HttpResponse(AliveResponse().AliveResponseObject(requestGetData = request.GET), content_type='application/json')

#Get data for API/Data Base

def apiData(request):
    from app.apiData.apiData import AliveAPI
    return JsonResponse(AliveAPI().aliveAPIObject())

def getApiDatabase(request):
    from app.apiData.apiData import data
    return JsonResponse(Data().Data(content_type='application/json'))