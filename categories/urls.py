from django.conf.urls import url, include
from .views import all_categories

urlpatterns = [
    url(r'^$', all_categories, name='categories'),
]