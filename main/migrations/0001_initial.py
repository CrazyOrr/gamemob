# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default=b'', blank=True)),
                ('cover', models.ImageField(default=b'covers/wow.jpg', upload_to=b'covers')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ReleaseDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.AddField(
            model_name='game',
            name='composer',
            field=models.ManyToManyField(related_name='main_game_composed', to='main.Person'),
        ),
        migrations.AddField(
            model_name='game',
            name='designer',
            field=models.ManyToManyField(related_name='main_game_designed', to='main.Person'),
        ),
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.ManyToManyField(related_name='main_game_developed', to='main.Company'),
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ManyToManyField(related_name='main_game', to='main.Genre'),
        ),
        migrations.AddField(
            model_name='game',
            name='mode',
            field=models.ManyToManyField(related_name='main_game', to='main.Mode'),
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ManyToManyField(related_name='main_game', to='main.Platform'),
        ),
        migrations.AddField(
            model_name='game',
            name='publisher',
            field=models.ManyToManyField(related_name='main_game_published', to='main.Company'),
        ),
        migrations.AddField(
            model_name='game',
            name='release_date',
            field=models.ManyToManyField(related_name='main_game', to='main.ReleaseDate'),
        ),
    ]
