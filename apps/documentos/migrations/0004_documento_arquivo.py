# Generated by Django 2.1.3 on 2018-11-20 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0003_auto_20181112_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(default=1, upload_to='documentos'),
            preserve_default=False,
        ),
    ]
