"""JordanPeterson URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views import static
from .settings import MEDIA_ROOT
from about.views import get_about
from accounts import urls as accounts_urls
from blog import urls as blog_urls
from blogcategories import urls as blogcategories_urls
from cart import urls as cart_urls
from checkout import urls as checkout_urls
from contact.views import contact
from home.views import get_index
from products import urls as products_urls
from products.views import all_products
from search import urls as search_urls
from categories import urls as categories_urls
from purchased import urls as purchased_urls





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name="index"),
    url(r'^about$', get_about, name="about"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^blog/', include(blog_urls)),
    url(r'^blogcategories/', include(blogcategories_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^categories/', include(categories_urls)),
    url(r'^checkout/', include(checkout_urls)),
    url(r'^contact/', contact, name='contact'),
    url(r'^products/', include(products_urls)),
    url(r'^purchased/', include(purchased_urls)),
    url(r'^search/', include(search_urls)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
]
