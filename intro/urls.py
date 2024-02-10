from django.urls import path
from app.views import index, respons_index, get_grocery_all, get_grocery_name, get_grocery_type, get_grocery_price, get_grocery_quantity, get_grocery_add

urlpatterns = [
    path('',index),
    path('home/', respons_index),
    #Grocery urls methods
    path('grocery/', get_grocery_all),
    path('grocery/name/<name>', get_grocery_name),
    path('grocery/type/<type>', get_grocery_type),
    path('grocery/price/<price>', get_grocery_price),
    path('grocery/quantity/<int:quantity>', get_grocery_quantity),
    path('grocery/add', get_grocery_add)
]


