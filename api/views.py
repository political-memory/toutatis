# coding: utf-8

# This file is part of toutatis.
#
# toutatis is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or any later version.
#
# toutatis is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU General Affero Public
# License along with toutatis.
# If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2015 Arnaud Fabre <af@laquadrature.net>

from representatives_votes.models import Dossier, Proposal, Vote
from rest_framework import viewsets, filters
from representatives_votes.serializers import (VoteSerializer,
                                               ProposalSerializer, ProposalDetailSerializer,
                                               DossierSerializer, DossierDetailSerializer)

class DossierViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows dossiers to be viewed.
    """
    
    queryset = Dossier.objects.all()
    serializer_class = DossierSerializer
    
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    filter_fields = {
        'fingerprint': ['exact'],
        'title': ['exact', 'icontains'],
        'reference': ['exact', 'icontains'],
    }
    
    search_fields = ('title', 'fingerprint', 'reference', 'text', 'proposals__title')
    ordering_fields = ('id', 'reference')
   
    
    def list(self, request):
        return super(DossierViewSet, self).list(request)

    def retrieve(self, request, pk=None):
        self.serializer_class = DossierDetailSerializer
        return super(DossierViewSet, self).retrieve(request, pk)


class ProposalViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows proposals to be viewed.
    """
    
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    
    filter_fields = {
        'fingerprint': ['exact'],
        'dossier__fingerprint': ['exact'],
        'title': ['exact', 'icontains'],
        'description': ['icontains'],
        'reference': ['exact', 'icontains'],
        'datetime': ['exact', 'gte', 'lte'],
        'kind': ['exact'],
    }
    
    search_fields = ('title', 'fingerprint', 'reference',
                     'dossier__fingerprint', 'dossier__title',
                     'dossier__reference')
    ordering_fields = ('id', 'reference')
    
    def list(self, request):
        return super(ProposalViewSet, self).list(request)

    def retrieve(self, request, pk=None):
        self.serializer_class = ProposalDetailSerializer
        return super(ProposalViewSet, self).retrieve(request, pk)


class VoteViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows proposals to be viewed.
    """
    
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    
    filter_fields = {
        'proposal__fingerprint': ['exact'],
        'position': ['exact'],
        'representative_name': ['exact', 'icontains'],
        'representative': ['exact']
    }
   
    def list(self, request):
        return super(VoteViewSet, self).list(request)

    def retrieve(self, request, pk=None):
        return super(VoteViewSet, self).retrieve(request, pk)
