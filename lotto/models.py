from django.db import models
import random

from pytz import timezone

# Create your models here.

class GuessNumbers(models.Model):
    name = models.CharField(max_length=24)
    text = models.CharField(max_length=255)
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5]')
    num_lotto = models.IntegerField(default=5)
    update_date = models.DateTimeField()

    def generate(self):
        self.lottos = ""
        origin = list(range(1,46))

        for i in range(0, self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) + '\n' # 로또번호를 str에 6개 번호 set 추가
        self.update_date = timezone.now()
        self.save() # GuessNumbers object를 DB에 저장

    def __str__(self) -> str:
        return f'pk {self.pk} : {self.name} - {self.text}'
