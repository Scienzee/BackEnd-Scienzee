import django


from django.urls import path
from dev.views import *

urlpatterns = [
    path('', home, name='home'),
    path('country/', country, name='country'),
    path('invalid-returns/', invalid_returns, name='invalid_returns'),
]