from tastypie.resources import ModelResource
from parltrack_votes.models import Proposal, ProposalPart, Vote
from parltrack_meps.models import MEP


class ProposalRessource(ModelResource):
    class Meta:
        queryset = Proposal.objects.all()
        resource_name = 'proposal'


class ProposalPartRessource(ModelResource):
    class Meta:
        queryset = ProposalPart.objects.all()
        resource_name = 'proposal_part'


class VoteRessource(ModelResource):
    class Meta:
        queryset = Vote.objects.all()
        resource_name = 'vote'


class MEPRessource(ModelResource):
    class Meta:
        queryset = MEP.objects.all()
        resource_name = 'mep'
