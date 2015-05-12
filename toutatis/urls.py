from django.conf.urls import include, url
from .views import home
urlpatterns = [
    url(r'^$', home),
    url(r'^export/', include('export_data.urls')),
]
