# Generated by Django 2.2.6 on 2019-10-07 19:37
from django.db import migrations


def forwards(apps, schema_editor):
    PackageVersion = apps.get_model(
        "repository",
        "PackageVersion"
    )
    for version in PackageVersion.objects.all():
        version.file.name = f"repository/packages/{version.file.name}"
        version.icon.name = f"repository/icons/{version.icon.name}"
        version.save()


def backwards(apps, schema_editor):
    PackageVersion = apps.get_model(
        "repository",
        "PackageVersion"
    )
    for version in PackageVersion.objects.all():
        version.file.name = version.file.name.replace("repository/packages/", "")
        version.icon.name = version.icon.name.replace("repository/icons/", "")
        version.save()


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0016_recache_versions'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
