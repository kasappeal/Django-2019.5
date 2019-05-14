from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):

    COPYRIGHT = 'RIG'
    COPYLEFT = 'LEF'
    CREATIVE_COMMONS = 'CC'

    LICENSES = [
        [COPYLEFT, 'Copyleft'],
        [COPYRIGHT, 'Copyright'],
        [CREATIVE_COMMONS, 'Creative Commons']
    ]

    PUBLIC = 'PUB'
    PRIVATE = 'PRI'

    VISIBILITY = [
        [PUBLIC, 'Public'],
        [PRIVATE, 'Private']
    ]

    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    license = models.CharField(max_length=3, choices=LICENSES)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=PUBLIC)
    owner = models.ForeignKey(User, related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
