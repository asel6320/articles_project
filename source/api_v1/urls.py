from django.urls import path

from api_v1.views import add, subtract, multiply, divide, get_csrf_token

app_name = 'api_v1'

urlpatterns = [
    path('add/', add, name='add'),
    path('get-token/', get_csrf_token, name='get_token'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide'),
]