from django.http import JsonResponse
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all().values()
    return JsonResponse(list(customers), safe=False)
