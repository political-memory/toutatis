import json
import hashlib

from datetime import datetime

from django.core.management.base import BaseCommand

from exported_data.models import ExportedRevision
from exported_data.utils import export_all_votes, CustomJSONEncoder


class Command(BaseCommand):
    help = 'Export all Votes to a ExportedRevision object'

    def handle(self, *args, **options):
        data = json.dumps(export_all_votes(), indent=4, cls=CustomJSONEncoder)
        checksum = hashlib.sha256(data).hexdigest()
        exported_revision = ExportedRevision.objects.filter(checksum=checksum)
        if exported_revision:
            exported_revision = exported_revision[0]
            exported_revision.last_check_datetime = datetime.now()
            exported_revision.save()
        else:
            ExportedRevision.objects.create(
                data=data,
                checksum=hashlib.sha256(data).hexdigest(),
                creation_datetime=datetime.now(),
                last_check_datetime=datetime.now()
            )
