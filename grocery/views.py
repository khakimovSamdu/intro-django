from django.http import HttpRequest, HttpResponse, JsonResponse
import json

data = {
    "1": {
            "name": "Apple",
            "quantity": 2,
            "price": 2.4,
            "type": "fruit"
        },
        "2": {
            "name": "Milk",
            "quantity": 1,
            "price": 2.5,
            "type": "dairy"
        },
        "3": {
            "name": "Carrot",
            "quantity": 2,
            "price": 1.5,
            "type": "vegetable"
        },
        "4": {
            "name": "Bread",
            "quantity": 1,
            "price": 1.5,
            "type": "bakery"
        },
        "5": {
            "name": "Eggs",
            "quantity": 1,
            "price": 2.5,
            "type": "dairy"
        }
}


def get_all(request: HttpRequest):
    return JsonResponse(data)

def get_add(request: HttpRequest):
    if request.method=="POST":
        item = request.body
        item = json.loads(item)
        data[len(data)+1] = item
        
        return JsonResponse(data)
    else: 
        return HttpResponse("Method error")

def get_by_id(request: HttpRequest, id: str):
    item = data[id]
    try :
        return JsonResponse(item)
    except:
        return HttpRequest("Key error")

def get_allprice(request: HttpRequest):
    narx=0.0
    for i in range(1,1+len(data)):
        narx+=(data[str(i)]['price'])
    return HttpResponse(f"Jami mahsulot narxi: {narx}")
