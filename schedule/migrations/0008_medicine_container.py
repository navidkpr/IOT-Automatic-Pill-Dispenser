# Generated by Django 2.1.7 on 2019-02-17 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_container_drug_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='container',
            field=models.IntegerField(default=0),
        ),
    ]
