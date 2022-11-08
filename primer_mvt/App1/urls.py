from django.urls import path

from App1.views import mostrar_familiares,mostrar_index

urlpatterns = [
    path('', mostrar_familiares),
    path('',mostrar_index),
]


