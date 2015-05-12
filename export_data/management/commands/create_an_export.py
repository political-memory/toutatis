import json
import hashlib

from django.utils import timezone
from django.core.management.base import BaseCommand

from export_data.models import ExportedRevision
from representatives_votes.utils import export_a_dossier

from representatives_votes.models import Dossier

class Command(BaseCommand):

    def handle(self, *args, **options):
        dossier_id = args[0]
        dossier = Dossier.objects.get(reference=dossier_id)
        self.create_export(json.dumps(export_a_dossier(dossier), indent=4), dossier_id)

    def create_export(self, data, dossier_id):
        checksum = hashlib.sha256(data).hexdigest()
        exported_revision = ExportedRevision.objects.filter(checksum=checksum)

        now = timezone.now()

        if exported_revision:
            exported_revision = exported_revision[0]
            exported_revision.last_check_datetime = now
            exported_revision.save()
        else:
            ExportedRevision.objects.create(
                data=data,
                dossier_reference=dossier_id,
                checksum=hashlib.sha256(data).hexdigest(),
                creation_datetime=now,
                last_check_datetime=now
            )
