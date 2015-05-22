from django.conf.urls import include, url
from django.contrib import admin
from .views import home


urlpatterns = [
    url(r'^$', home),
    url(r'^export/', include('export_data.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls))
]
