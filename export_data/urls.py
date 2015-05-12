from django.conf.urls import patterns, url

from export_data import views

urlpatterns = patterns('',
    url(r'^(?P<dossier_reference>.+)/$', views.get_dossier_data),
    # url(r'^latest/(?P<kind>\w+)/checksum/$', views.get_lastest_checksum),    
    # url(r'^latest/$', views.get_lastest_data),
    # url(r'^latest/(?P<kind>\w+)/$', views.get_lastest_data),
)
