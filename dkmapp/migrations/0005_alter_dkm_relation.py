# Generated by Django 4.1 on 2023-03-26 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dkmapp', '0004_alter_dkm_relation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dkm',
            name='relation',
            field=models.CharField(blank=True, choices=[('inti', 'inti'), ('fasilitator', 'fasilitator'), ('anggota', 'anggota')], max_length=200, null=True),
        ),
    ]
