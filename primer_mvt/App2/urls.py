from django.urls import path
from App2.views import mostrar_index

urlpatterns = [
    path('',mostrar_index),
]
