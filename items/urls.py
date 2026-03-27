from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.all_items, name='all_items'),
    path('add/', views.add_item, name='add_item'),
]
