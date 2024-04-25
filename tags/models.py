from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # What tag applyed to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # [3] Things to make Generic Relationship :-
    # Content Type (product, video, article)
    # Object ID
    # Content Object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
