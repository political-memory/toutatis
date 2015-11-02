from django.conf.urls import include, url
from django.contrib import admin
from django.views import generic

from rest_framework import routers

from representatives.api import (
    ConstituencyViewSet,
    GroupViewSet,
    MandateViewSet,
    RepresentativeViewSet,
)

from representatives_votes.api import (
    DossierViewSet,
    ProposalViewSet,
    VoteViewSet,
)

router = routers.DefaultRouter()

router.register(r'constituencies', ConstituencyViewSet)
router.register(r'dossiers', DossierViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'mandates', MandateViewSet)
router.register(r'proposals', ProposalViewSet)
router.register(r'representatives', RepresentativeViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = [
    url(r'^$', generic.RedirectView.as_view(url='/api/')),
    url(r'^api/', include(router.urls)),
]
