# Generated by Django 4.1 on 2023-03-25 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_dkm', models.CharField(max_length=20)),
                ('nim_nidn', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('gender', models.CharField(choices=[('male', 'Laki-laki'), ('female', 'Perempuan')], max_length=12, null=True)),
                ('relation', models.CharField(blank=True, choices=[('suami', 'suami'), ('istri', 'istri'), ('anak perempuan', 'anak perempuan'), ('anak laki-laki', 'anak laki-laki'), ('ayah', 'ayah'), ('ibu', 'ibu')], max_length=200, null=True)),
                ('photo', models.ImageField(null=True, upload_to='profil')),
                ('mid', models.IntegerField(blank=True, null=True)),
                ('fid', models.IntegerField(blank=True, null=True)),
                ('pids', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, choices=[('aktif', 'aktif'), ('tidak aktif', 'tidak aktif')], max_length=200, null=True)),
            ],
        ),
    ]