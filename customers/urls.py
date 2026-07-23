from django.urls import path
from .views import customer_list

urlpatterns = [
    path('list/', customer_list),
]
