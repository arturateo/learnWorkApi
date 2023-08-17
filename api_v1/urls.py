from django.urls import path

from api_v1.views import json_add_view, json_divide_view, json_multiply_view, json_subtract_view

app_name = 'api_v1'

urlpatterns = [
    path('add/', json_add_view, name='add'),
    path('subtract/', json_subtract_view, name='subtract'),
    path('multiply/', json_multiply_view, name='multiply'),
    path('divide/', json_divide_view, name='divide'),
]
