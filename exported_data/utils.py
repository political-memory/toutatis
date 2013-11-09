from django.core.serializers.json import DjangoJSONEncoder
from decimal import Decimal
from datetime import datetime, date
import time

from parltrack_votes.models import Proposal
from django.db import transaction


def export_proposal(i, proposal):
    print i
    return {
        'code_name': proposal.code_name,
        'title': proposal.title,
        'date': proposal.date,
        'parts': [export_part(part) for part in proposal.proposalpart_set.all()]
    }


def export_part(part):
    return {
        'datetime': part.datetime,
        'subject': part.subject,
        'part': part.part,
        'votes_for': [vote.mep.ep_id for vote in part.vote_set.filter(choice='for')],
        'votes_against': [vote.mep.ep_id for vote in part.vote_set.filter(choice='against')],
        'votes_abstension': [vote.mep.ep_id for vote in part.vote_set.filter(choice='abstension')],
    }


def export_vote(vote):
    return {
        'choice': vote.name,
        'mep': vote.mep.ep_id if vote.mep else None,
    }


def export_all_votes():
    with transaction.commit_on_success():
        return [export_proposal(i, proposal) for i, proposal in enumerate(Proposal.objects.all(),)]


class CustomJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, datetime):
            return time.mktime(obj.timetuple()) * 1000
        if isinstance(obj, date):
            return str(obj)
        return super(CustomJSONEncoder, self).default(obj)
