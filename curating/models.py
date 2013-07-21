from django.db import models
from parltrack_votes.models import ProposalPart
from parltrack_meps.models import MEP


class CuratedProposalPart(models.Model):
    proposal_part = models.OneToOneField(ProposalPart)
    meps = models.ManyToManyField(MEP)
