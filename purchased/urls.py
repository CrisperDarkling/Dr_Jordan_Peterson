from django.conf.urls import url, include
from .views import purchased

urlpatterns = [
    url(r'^$', purchased, name='purchased'),
    url(r'^$', purchased, name='purchased'),
]