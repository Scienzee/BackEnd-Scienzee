from django.shortcuts import render

def home(request):
    token='active'
    return render(request, 'dev-authorization.html', locals())

def country(request):
    paises = 'active'
    return render(request, 'dev-country.html', locals())

def invalid_returns(request):
    invalid_return = 'active'
    return render(request, 'dev-invalid-return.html', locals())
