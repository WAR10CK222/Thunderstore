# Generated by Django 2.1.2 on 2019-05-07 18:39

import backblaze_b2.storage
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import thunderstore.repository.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repository', '0007_rename_pinned'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploaderIdentity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UploaderIdentityMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('owner', 'owner'), ('member', 'member')], default='member', max_length=64)),
                ('identity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='repository.UploaderIdentity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_identities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='package',
            name='maintainers',
        ),
        migrations.AlterField(
            model_name='packageversion',
            name='file',
            field=models.FileField(storage=backblaze_b2.storage.BackblazeB2Storage(), upload_to=thunderstore.repository.models.get_version_zip_filepath),
        ),
        migrations.AlterUniqueTogether(
            name='uploaderidentitymember',
            unique_together={('user', 'identity')},
        ),
    ]