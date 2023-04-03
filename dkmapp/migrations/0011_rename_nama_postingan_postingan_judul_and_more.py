# Generated by Django 4.1 on 2023-03-29 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dkmapp', '0010_alter_dkm_jabatan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postingan',
            old_name='nama_postingan',
            new_name='judul',
        ),
        migrations.AddField(
            model_name='postingan',
            name='caption',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='postingan',
            name='post',
            field=models.ImageField(null=True, upload_to='post'),
        ),
    ]
