# Generated by Django 3.2.13 on 2022-04-14 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('description', models.TextField(verbose_name='내용')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='blog/%Y/%m/%d', verbose_name='이미지')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
