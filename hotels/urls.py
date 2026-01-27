from django.urls import path
from .views import hotel_list, hotel_create, hotel_update, hotel_delete


urlpatterns = [
    
    path('', hotel_list),
    path('create/', hotel_create),
    path('<int:id>/update/', hotel_update),
    path('<int:id>/delete/', hotel_delete),
]
