# Generated by Django 4.0 on 2022-02-22 17:55

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='short_description',
            field=mdeditor.fields.MDTextField(blank=True, null=True),
        ),
    ]