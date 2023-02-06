from django.http import JsonResponse

def getRoutes(request):
    routes = {
        {"GET": "/api/projects"},
        {"GET": "/api/projects/id"},
        {"GET": "/api/projects/"},
    }



    return JsonResponse(routes)

