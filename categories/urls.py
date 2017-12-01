from django.conf.urls import url, include
from .views import all_categories
from products.views import products_by_category

urlpatterns = [
    url(r'^$', all_categories, name='categories'),
    url(r'^(\d+)$', products_by_category, name='products_by_category'),
]