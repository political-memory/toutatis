from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.constants import ALL
# from representatives.models import Representative
from representatives_votes.models import Dossier, Proposal


class DossierResource(ModelResource):    
    proposals = fields.ToManyField(
        'api.api.ProposalResource',
        'proposal_set',
        full=True,
        full_detail=True,
        full_list=False
    )
    
    class Meta:
        queryset = Dossier.objects.all()
        allowed_methods = ['get']
        resource_name = 'dossiers'
        filtering = {
            'title': ALL,
            'reference': ALL
        }


class ProposalResource(ModelResource):
    dossier = fields.ToOneField(DossierResource, 'dossier')
        
    votes = fields.ListField(
        attribute='vote_api_list',
        use_in='detail'
    )

    class Meta:
        queryset = Proposal.objects.all()
        resource_name = 'proposals'



