# Generated by Django 4.2.2 on 2023-07-16 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_postcomments_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomments',
            old_name='body',
            new_name='comment',
        ),
    ]