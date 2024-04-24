from django.db import models
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Tag (models.Model):
  label = models.CharField(max_length=255)

class TaggedItem (models.Model):
  # What tag applyed to what object
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
  # Type (product, video, article)
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  # ID
  object_id = models.PositiveIntegerField()