from django.conf.urls import url
from .views import *

from . import views
 
urlpatterns = [
    url(r'^$', contact_page, name="contact_page"),

]