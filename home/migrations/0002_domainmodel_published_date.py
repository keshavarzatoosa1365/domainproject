# Generated by Django 3.2.7 on 2021-09-19 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='domainmodel',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان انتشار'),
        ),
    ]