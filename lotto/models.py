from django.db import models

# Create your models here.

class GuessNumbers(models.Model):
    name = models.CharField(max_length=24)
    text = models.CharField(max_length=255)
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5]')
    num_lotto = models.IntegerField(default=5)
    update_date = models.DateTimeField()