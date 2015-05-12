from django.db import models


class ExportedRevision(models.Model):
    data = models.TextField()
    dossier_reference = models.CharField(max_length=200)
    checksum = models.CharField(max_length=255, unique=True)
    creation_datetime = models.DateTimeField()
    last_check_datetime = models.DateTimeField()

    class Meta:
        ordering = ['-last_check_datetime']
