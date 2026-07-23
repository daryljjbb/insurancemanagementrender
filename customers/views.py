from django.http import JsonResponse

def customer_list(request):
    customers = [
        {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "phone": "555-1234",
            "address": "123 Main St"
        },
        {
            "id": 2,
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane@example.com",
            "phone": "555-5678",
            "address": "456 Oak Ave"
        }
    ]
    return JsonResponse(customers, safe=False)
