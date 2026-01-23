from django.urls import path
from .views import hotel_list, hotel_create, hotel_update, hotel_delete

urlpatterns = [
    path('api/hotels/', hotel_list),
    path('api/hotels/create/', hotel_create),
    path('api/hotels/<int:id>/update/', hotel_update),
    path('api/hotels/<int:id>/delete/', hotel_delete),
]
