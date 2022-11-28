# Generated by Django 4.1.3 on 2022-11-26 13:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunSQL('CREATE SCHEMA IF NOT EXISTS content'),
        migrations.CreateModel(
            name='FilmWork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique key')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(
                    null=True, verbose_name='description')),
                ('creation_date', models.DateField(null=True,
                 verbose_name='creation date')),
                ('file_path', models.FileField(null=True, upload_to='movies/',
                verbose_name='file')),
                ('rating', models.FloatField(null=True, validators=[
                    django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='rating')),
                ('type', models.CharField(choices=[(
                'movies', 'movies'), ('tv_show', 'tv_show')],
                    default='movies', max_length=20, verbose_name='type')),
                ('created', models.DateTimeField(auto_now_add=True,
                                                 verbose_name='created')),
                ('modified',
                 models.DateTimeField(auto_now=True, verbose_name='modified')),

            ],
            options={
                'verbose_name': 'film work',
                'verbose_name_plural': 'films work',
                'db_table': 'content"."film_work',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique key')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(
                    null=True, verbose_name='description')),
                ('created', models.DateTimeField(auto_now_add=True,
                                                 verbose_name='created')),
                ('modified',
                 models.DateTimeField(auto_now=True, verbose_name='modified')),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
                'db_table': 'content"."genre',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique key')),
                ('full_name', models.CharField(max_length=150, verbose_name='full name')),
                ('created', models.DateTimeField(auto_now_add=True,
                                                 verbose_name='created')),
                ('modified',
                 models.DateTimeField(auto_now=True, verbose_name='modified')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
                'db_table': 'content"."person',
            },
        ),
        migrations.CreateModel(
            name='PersonFilmWork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique key')),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork', verbose_name='film work')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person', verbose_name='person')),
                ('role', models.TextField(verbose_name='role')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'content"."person_film_work',
                'unique_together': {('role', 'person', 'film_work')},
            },
        ),
        migrations.CreateModel(
            name='GenreFilmWork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique key')),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork', verbose_name='film work')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre', verbose_name='genre')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'content"."genre_film_work',
                'unique_together': {('genre', 'film_work')},
            },
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(through='movies.GenreFilmWork', to='movies.genre', verbose_name='genres'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='person',
            field=models.ManyToManyField(through='movies.PersonFilmWork', to='movies.person', verbose_name='person'),
        ),
    ]
