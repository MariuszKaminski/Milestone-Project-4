from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.

def all_menu_items(request):
    """ A view to show individual product details """

    menu_items = Item.objects.all()

    context = {
        'menu_items': menu_items,
    }
    
    return render(request, 'menu_items/menu_items.html', context)

from django.shortcuts import render
from .models import Item

# Create your views here.

def item_detail(request, item_id):
    """ A view to show all menu items, including sorting and search queries """

    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }
    
    return render(request, 'menu_items/item_detail.html', context)
