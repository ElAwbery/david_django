from django.shortcuts import render, redirect
from david_app.models import David_app
# from demoapp.models import Demoapp
from django.http import HttpResponse

# Request is a Django object that gets passed around everywhere
# Views must return an http response object

# The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.

def david_app(request):
    data=David_app.objects.all()
    print(data)
    return render(request, 'david_app/content.html', {'data':data,})