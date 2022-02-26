

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_project_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='short_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
