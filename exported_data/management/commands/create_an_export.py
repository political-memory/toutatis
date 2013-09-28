import json


from django.core.management.base import BaseCommand

from exported_data.models import ExportedRevision
from exported_data.utils import export_all_votes, CustomJSONEncoder


class Command(BaseCommand):
    help = 'Export all Votes to a ExportedRevision object'

    def handle(self, *args, **options):
        data = json.dumps(export_all_votes(), indent=4, cls=CustomJSONEncoder)
        ExportedRevision.create_revision_with_data(data)
