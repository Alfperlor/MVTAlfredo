from django.urls import path
from App1.views import mostrar_familia

urlpatterns = [
    path('', mostrar_familia)
]
