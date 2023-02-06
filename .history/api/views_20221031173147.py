from django.http import JsonResponse

def getRoutes(request):
    routes = {
        {"GET": "/api/projects"},
        {"GET": "/api/projects/id"},
        {"GET": "/api/projects/id/vote"},
        
        
        {"POST": "/api/users/id/vote"},
        
    }



    return JsonResponse(routes)

