# Generated by Django 3.2.7 on 2021-10-08 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0002_alter_upload_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='action',
            field=models.CharField(choices=[('NO_FILTER', 'no filter'), ('NEGATIVE', 'negative'), ('GREYSCALE', 'greyscale'), ('BRIGHTENING', 'brightening'), ('ARITMETIKA', 'aritmetika'), ('BOOLEAN', 'boolean'), ('GEOMETRI', 'geometri')], max_length=50),
        ),
    ]
