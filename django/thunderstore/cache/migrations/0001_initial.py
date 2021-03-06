# Generated by Django 3.0.4 on 2020-10-03 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_updated', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(db_index=True, max_length=512, unique=True)),
                ('content', models.BinaryField(blank=True, null=True)),
                ('expires_on', models.DateTimeField(blank=True, null=True)),
                ('hits', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
