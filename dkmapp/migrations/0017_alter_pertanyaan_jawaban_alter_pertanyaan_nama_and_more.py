# Generated by Django 4.1 on 2023-03-30 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dkmapp', '0016_alter_postingan_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pertanyaan',
            name='jawaban',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='pertanyaan',
            name='nama',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='pertanyaan',
            name='nim',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='pertanyaan',
            name='pemberi_jawaban',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dkmapp.dkm'),
        ),
    ]
