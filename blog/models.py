from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField('제목', max_length=50)
    description = models.TextField('내용')
    photo = models.ImageField('이미지', blank=True, null=True, upload_to='blog/%Y/%m/%d')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title