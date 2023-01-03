from django.urls import path
from .views import ClientesView, ClienteAddView, ClienteUpDateView

urlpatterns = [
    path('clientes', ClientesView.as_view(), name='clientes'),
    path('cliente/adicionar/', ClienteAddView.as_view(), name='cliente_adicionar'),
    path('<int:pk>/cliente/editar/', ClienteUpDateView.as_view(), name='cliente_editar'),
]