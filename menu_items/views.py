from django.shortcuts import render
from .models import Item

# Create your views here.

def all_menu_items(request):
    """ A view to show all menu items, including sorting and search queries """

    menu_items = Item.objects.all()

    context = {
        'menu_items': menu_items,
    }
    
    return render(request, 'menu_items/menu_items.html', context)
