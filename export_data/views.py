from django.http import HttpResponse, HttpResponseNotFound
from .models import ExportedRevision

def get_dossier_data(request, dossier_reference):
     exported_revision = ExportedRevision.objects.filter(dossier_reference=dossier_reference)
     if not exported_revision:
         return HttpResponseNotFound('<h1>Page not found</h1>')

     return HttpResponse(exported_revision.latest('last_check_datetime').data)
