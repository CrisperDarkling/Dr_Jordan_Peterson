from django.conf.urls import url, include
from .views import youtube_categories
from blog.views import youtube_by_category

urlpatterns = [
    url(r'^$', youtube_categories, name='youtubecategories'),
    url(r'^(\d+)$', youtube_by_category, name='youtube_by_category'),
]