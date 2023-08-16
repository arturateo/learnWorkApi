from django.urls import path

from api_v1.views import json_add_view, json_divide_view, json_multiply_view, json_subtract_view

project_name = 'api_v1'

urlpatterns = [
    path('add/', json_add_view),
    path('subtract/', json_divide_view),
    path('multiply/', json_multiply_view),
    path('divide/', json_subtract_view),
]
