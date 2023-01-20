from django.db import models
from django.urls import reverse


class Wage(models.Model):
    position = models.CharField(max_length=100, help_text='Position wage per month')
    monthly = models.IntegerField()

    def _get_yearly(self):
        return self.monthly * 13
    yearly = property(_get_yearly)

    class Meta:
        ordering = ['-position', '-monthly']

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.position

