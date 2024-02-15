from django.urls import path
from .views import index, respons_index, get_grocery_all, get_grocery_name, get_grocery_type, get_grocery_price, get_grocery_quantity, get_grocery_add

urlpatterns = [
    path('index/',index),
    path('home/', respons_index),
    #Grocery urls methods
    path('', get_grocery_all),
    path('name/<name>', get_grocery_name),
    path('type/<type>', get_grocery_type),
    path('price/<price>', get_grocery_price),
    path('quantity/<int:quantity>', get_grocery_quantity),
    path('add', get_grocery_add),

]


