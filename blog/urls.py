from django.urls import path
from .views import Home
# from . import views


urlpatterns = [
    # path('', views.home, name="home"),
    path('', Home.as_view(), name='home'),
]
