from django.shortcuts import render, redirect, HttpResponse
from ..first_app.models import User
from .models import Poke

# Create your views here.
def pokes(request):
    print '*** pokes ***'
    if not request.session['user_id']:
        return redirect('/')
    try:
        request.session['poke']
    except:
        request.session['poke'] = 0

    try:
        request.session['activities']
    except:
        request.session['activities'] = []
    context = {
        'users': User.objects.exclude(id = request.session['user_id']),
        'pokes': Poke.objects.all(),
    }
    return render(request, 'second_app/poke.html', context)

def poke_proccesser(request):
    print '*** poke_proccesser ***'
    if not request.session['user_id']:
        return redirect('/')

    try:
        request.session['activities'].insert(0,{{request.session.name}} + 'poked you' + str(poke.number_of_pokes) + 'times.')
        print request.session['activities']
        return redirect('/pokes')
    except:
        return redirect('/pokes')

def add_poke(request):
    print '********** add_poke *******'
    try:
        print '***********'
        poke = Poke.objects.get(id = id)
        poke.number_of_pokes += 1
        poke.save()
        print poke
        return redirect('/pokes')
    except:
        return redirect('/pokes')
