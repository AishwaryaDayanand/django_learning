# Generated by Django 4.1 on 2022-08-19 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_tag_projects_vate_ratio_projects_vote_total_review_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
