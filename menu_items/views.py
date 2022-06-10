from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Item, Category

# Create your views here.

def all_menu_items(request):
    """ A view to show individual product details """

    menu_items = Item.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                menu_items = menu_items.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            menu_items = menu_items.order_by(sortkey)


        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            menu_items = menu_items.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search critieria!")
                return redirect(reverse('menu_items'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            menu_items = menu_items.filter(queries)
    
    current_sorting = f'{sort}_{direction}'

    context = {
        'menu_items': menu_items,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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
