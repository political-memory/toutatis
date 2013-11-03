from django.conf.urls import patterns, url

from exported_data.views import get_lastest_data, get_lastest_checksum

urlpatterns = patterns('',
    url(r'^latest/$', get_lastest_data),
    url(r'^latest/checksum/$', get_lastest_checksum),
)
