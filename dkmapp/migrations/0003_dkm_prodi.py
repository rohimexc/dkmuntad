# Generated by Django 4.1 on 2023-03-25 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dkmapp', '0002_rename_family_dkm'),
    ]

    operations = [
        migrations.AddField(
            model_name='dkm',
            name='prodi',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
