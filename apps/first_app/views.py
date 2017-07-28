from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User


# Create your views here.
def index(request):
    print '*** index ***'
    # User.objects.all().delete()
    return render(request, 'first_app/index.html')

def register(request):
    print '*** register ***'
    results = User.objects.registerVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
    else:
        user = User.objects.createUser(request.POST)
        messages.success(request, 'User has been created!')

    return redirect('/')

def login(request):
    print '*** login ***'
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['name'] = results['user'].name
        request.session['user_id'] = results['user'].id
        return redirect('/pokes')

def logout(request):
    print '*** logout ***'
    request.session['user_id']=None
    return redirect('/')
