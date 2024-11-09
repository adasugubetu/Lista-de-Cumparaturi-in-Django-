from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Produs

def index(request):
    produse = Produs.objects.all()
    return render(request, 'lista_cumparaturi/index.html', {'produse': produse})

def adauga_produs(request):
    if request.method == 'POST':
        nume = request.POST.get('nume')
        if nume:
            # Create a new product and save it to the database
            Produs.objects.create(nume=nume, cumparat=False)
            return redirect(reverse('index'))
    return render(request, 'lista_cumparaturi/adauga.html')

def sterge_produs(request, produs_id):
    # Delete the product from the database
    Produs.objects.filter(id=produs_id).delete()
    return redirect(reverse('index'))


def marcheaza_cumparat(request, produs_id):
    try:
        produs = Produs.objects.get(id=produs_id)
        produs.cumparat = True  # Mark as bought
        produs.save()  # Save to database
    except Produs.DoesNotExist:
        pass

    return redirect(reverse('index'))
