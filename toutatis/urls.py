from django.conf.urls import patterns, include, url
from tastypie.api import Api
from api.api import ProposalRessource, ProposalPartRessource, VoteRessource, MEPRessource

v1_api = Api(api_name='v1')
v1_api.register(ProposalRessource())
v1_api.register(ProposalPartRessource())
v1_api.register(VoteRessource())
v1_api.register(MEPRessource())

# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'toutatis.views.home', name='home'),
    # url(r'^toutatis/', include('toutatis.foo.urls')),
    url(r'^api/', include(v1_api.urls)),

    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
