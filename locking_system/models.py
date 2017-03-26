from django.db import models


class Resource(models.Model):

    RELEASED = 0
    LOCKED = 1
    STATUS_OPTIONS = (
        (RELEASED, 'Released'),
        (LOCKED, 'Locked'),
    )
    name = models.CharField(max_length=60, unique=True)
    status = models.SmallIntegerField(choices=STATUS_OPTIONS, default=RELEASED)
    last_action_time = models.DateTimeField(auto_now=True)
