from django.conf.urls import url, include
from tastypie.api import Api
from api import DossierResource, ProposalResource, VoteResource

v1_api = Api(api_name='v1')
v1_api.register(DossierResource())
v1_api.register(ProposalResource())
v1_api.register(VoteResource())

urlpatterns = [
    url(r'^',  include(v1_api.urls))
]
