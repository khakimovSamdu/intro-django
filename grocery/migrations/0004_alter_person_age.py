# Generated by Django 5.0.1 on 2024-02-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_person_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.TextField(),
        ),
    ]
