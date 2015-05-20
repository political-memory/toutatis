from django.conf.urls import patterns, url
from export_data import views
urlpatterns = patterns('',
    url(r'^(?P<dossier_reference>.+)/$', views.get_dossier_data),
)
