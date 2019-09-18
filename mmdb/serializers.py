from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from mmdb.models import customer

def data_list(request):
    if request.method == 'GET':
        customer = customer.objects.all()
        return JsonResponse(customer, safe=False)