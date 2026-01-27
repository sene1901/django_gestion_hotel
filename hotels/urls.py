from django.urls import path
from .views import hotel_list,  HotelCreateView, hotel_update, hotel_delete


urlpatterns = [
    
    path('', hotel_list),
    path("create/", HotelCreateView.as_view(), name="hotel-create"),
    path('<int:id>/update/', hotel_update),
    path('<int:id>/delete/', hotel_delete),
]
