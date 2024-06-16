from django.db import models

# Create your models here.
class Subscriber(models.Model):
    SUBSCRIBE_WEEKLY = 'W'
    SUBSCRIBE_MONTHLY = 'M'

    SUBSCRIBE_CHOICES = (
        (SUBSCRIBE_WEEKLY,"Subscribe Weekly"),
        (SUBSCRIBE_MONTHLY,"Subscribe Monthly")
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    subscribe_type = models.CharField(max_length=1,choices=SUBSCRIBE_CHOICES,default=SUBSCRIBE_WEEKLY)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'