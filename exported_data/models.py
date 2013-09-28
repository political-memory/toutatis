import hashlib
from datetime import datetime

from django.db import models


class ExportedRevision(models.Model):
    data = models.TextField()
    checksum = models.CharField(max_length=255, unique=True)
    creation_datetime = models.DateTimeField()
    last_check_datetime = models.DateTimeField()

    class Meta:
        ordering = ['-last_check_datetime']
        get_latest_by = 'last_check_datetime'

    @staticmethod
    def create_revision_with_data(data):
        """ Add a revison of the data, if the data exists in db update
        last_check_datetime otherwhise create it."""
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
