from django.urls import path
from app.views import index, respons_index
from grocery.views import get_all, get_add, get_by_id, get_allprice

urlpatterns = [
    path('',index),
    path('home/', respons_index),
    #Grocery urls methods

    path('all/', get_all),
    path('add/', get_add),
    path('id/<id>', get_by_id),
    path('sumprice/', get_allprice)
]


