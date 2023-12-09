from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Pizza

# Create your views here.

# /menu
def index(resuest):
    '''
    # Recuperation des pizzas stocké en base de donées
    pizzas_names_and_price = [pizza.nom + " : " +  str(pizza.prix) + " €" for pizza in pizzas]
    pizzas_names_and_price_str = ", ".join(pizzas_names_and_price)
    return HttpResponse("Les pizzas :" + pizzas_names_and_price_str)
    '''
    pizzas = Pizza.objects.all().order_by('prix')
    return render(resuest, 'menu/index.html', context= {'pizzas':pizzas})
    


