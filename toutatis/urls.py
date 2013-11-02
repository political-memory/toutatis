from django.conf.urls import patterns, include, url

from tastypie.api import Api
from api.api import ProposalRessource, ProposalPartRessource, VoteRessource, MEPRessource

v1_api = Api(api_name='v1')
v1_api.register(ProposalRessource())
v1_api.register(ProposalPartRessource())
v1_api.register(VoteRessource())
v1_api.register(MEPRessource())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    url(r'^', include('exported_data.urls')),
)
