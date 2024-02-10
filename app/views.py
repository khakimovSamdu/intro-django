from django.http import HttpRequest, HttpResponse, JsonResponse
import json
from tinydb import TinyDB, Query
q = Query()

db = TinyDB('db.json', indent=4)
data = db.table('grocery')

def index(request: HttpRequest):
    a = int(request.GET.get('a','0'))
    b = int(request.GET.get('b','0'))
    data = {
        "a":a,
        "b":b
    }
    return JsonResponse(data)

def respons_index(request: HttpRequest):
    if request.method == 'POST':
        data = request.POST
        body = request.body
        # Convert bytes to string
        body = body.decode('utf-8')
        # Convert string to dictionary
        data = json.loads(body)
        
    return HttpResponse(data['a']+data['b'])

#Grocory methods
def get_grocery_all(request: HttpRequest):
    f = {"grocery":data.all()}
    return JsonResponse(f)

def get_grocery_name(request: HttpRequest, name: str):
    f = data.search(q.name==name)
    return JsonResponse({"name":f})

def get_grocery_type(request: HttpRequest, type: str):
    f = data.search(q.type==type)
    return JsonResponse({"type":f})

def get_grocery_price(request: HttpRequest, price: float):
    f = data.search(q.price==float(price))
    return JsonResponse({"price":f})

def get_grocery_quantity(request: HttpRequest, quantity):
    f = data.search(q.quantity==quantity)
    return JsonResponse({"quantity":f})

def get_grocery_add(request: HttpRequest):
    if request.method=="POST":
        f = request.POST
        body = request.body
        body=body.decode('utf-8')
        f = json.loads(body)
        data.insert(f)
        return JsonResponse({"grocery":data.all()})
