from django.contrib import admin
from .models import Pizza

# Pour personnaliser l'affichage des produits 
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['nom', 'ingredients', 'vegetarienne', 'prix']

# Ajouter notre model à l'interface d'administration 
admin.site.register(Pizza, PizzaAdmin)


