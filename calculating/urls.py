from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from calculating.views import HomeView

app_name = 'calculating'

urlpatterns = [
    path('', HomeView.as_view(), name="home_page")
]
