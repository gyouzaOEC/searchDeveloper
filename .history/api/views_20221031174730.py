from django.http import JsonResponse
from rest_framework import 
from  import 

def getRoutes(request):
    routes = [
        {"GET": "/api/projects"},
        {"GET": "/api/projects/id"},
        {"GET": "/api/projects/id/vote"},
        
        
        {"POST": "/api/users/token/"},
        {"POST": "/api/users/token/refresh"},
    ]

    return JsonResponse(routes,safe=False)

