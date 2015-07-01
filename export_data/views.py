import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from representatives_votes.models import Dossier
from representatives_votes.tasks import export_a_dossier

"""
Get dossier from exported revision

def get_dossier_data(request, dossier_reference):
     exported_revision = ExportedRevision.objects.filter(dossier_reference=dossier_reference)
     if not exported_revision:
         return HttpResponseNotFound('<h1>Page not found</h1>')

     return HttpResponse(exported_revision.latest('last_check_datetime').data)
"""

def get_dossier_data(request, dossier_reference):
     dossier = get_object_or_404(Dossier, reference=dossier_reference)
     exported_data = json.dumps(export_a_dossier(dossier))
     return HttpResponse(exported_data, content_type="text/plain")
