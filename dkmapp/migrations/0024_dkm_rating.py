# Generated by Django 4.1 on 2023-04-02 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dkmapp', '0023_remove_ulasan_pemberi_ulasan'),
    ]

    operations = [
        migrations.AddField(
            model_name='dkm',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
