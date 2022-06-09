from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_menu_items, name='menu_items'),
    path('<item_id>', views.item_detail, name='item_detail'),
]