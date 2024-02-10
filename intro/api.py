# from django.http import HttpRequest, HttpResponse, JsonResponse
# import json
# def index(request: HttpRequest):
#     a = int(request.GET.get('a','0'))
#     b = int(request.GET.get('b','0'))
#     data = {
#         "a":a,
#         "b":b
#     }
#     return JsonResponse(data)
# def respons_index(request: HttpRequest):
#     if request.method == 'POST':
#         data = request.POST
#         body = request.body
#         # Convert bytes to string
#         body = body.decode('utf-8')
#         # Convert string to dictionary
#         data = json.loads(body)
        
#     return HttpResponse(data['a']+data['b'])
