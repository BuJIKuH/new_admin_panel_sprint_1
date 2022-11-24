# Generated by Django 4.1.3 on 2022-11-23 13:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmwork',
            fields=[
                ('id',
                 models.UUIDField(
                    default=uuid.uuid4,
                    editable=False,
                    primary_key=True,
                    serialize=False,
                    verbose_name='Уникальный ключ'
                 )
                 ),
                ('created',
                 models.DateTimeField(
                    auto_now_add=True,
                    verbose_name='Дата создания записи'
                 )
                 ),
                ('modified', models.DateTimeField(
                    auto_now=True,
                    verbose_name='Дата изменения записи'
                 )
                 ),
                ('title', models.CharField(
                    max_length=255,
                    verbose_name='Название')),
                ('description',
                 models.TextField(
                    blank=True,
                    verbose_name='Описание'
                 )
                 ),
                ('creation_date',
                 models.DateField(
                    blank=True,
                    verbose_name='Дата премьеры'
                 )
                 ),
                ('rating', models.FloatField(
                    blank=True,
                    validators=[
                        django.core.validators.MinValueValidator(0),
                        django.core.validators.MaxValueValidator(100)],
                    verbose_name='Рейтинг'
                )
                 ),
                ('type',
                 models.CharField(
                    blank=True, choices=[
                        ('movies', 'Movie'),
                        ('tv_show', 'Tv Show')
                     ],
                    default='movies',
                    max_length=20,
                    verbose_name='Тип'
                 )
                 ),
            ],
            options={
                'verbose_name': 'Кинопроизведение',
                'verbose_name_plural': 'Кинопроизведения',
                'db_table': 'content"."film_work',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id',
                 models.UUIDField(
                    default=uuid.uuid4,
                    editable=False,
                    primary_key=True,
                    serialize=False,
                    verbose_name='Уникальный ключ'
                 )
                 ),
                ('created',
                 models.DateTimeField(
                    auto_now_add=True,
                    verbose_name='Дата создания записи'
                 )
                 ),
                ('modified',
                 models.DateTimeField(
                    auto_now=True,
                    verbose_name='Дата изменения записи'
                 )
                 ),
                ('name',
                 models.CharField(
                    max_length=255,
                    verbose_name='Название'
                 )
                 ),
                ('description',
                 models.TextField(
                    blank=True,
                    verbose_name='Описание'
                 )
                 ),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'db_table': 'content"."genre',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(
                    default=uuid.uuid4,
                    editable=False,
                    primary_key=True,
                    serialize=False,
                    verbose_name='Уникальный ключ'
                )
                 ),
                ('created',
                 models.DateTimeField(
                    auto_now_add=True,
                    verbose_name='Дата создания записи'
                 )
                 ),
                ('modified',
                 models.DateTimeField(
                    auto_now=True,
                    verbose_name='Дата изменения записи'
                 )
                 ),
                ('full_name',
                 models.CharField(
                    max_length=150,
                    verbose_name='Полное имя'
                 )
                 ),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
                'db_table': 'content"."person',
            },
        ),
        migrations.CreateModel(
            name='PersonFilmwork',
            fields=[
                ('id',
                 models.UUIDField(
                    default=uuid.uuid4,
                    editable=False,
                    primary_key=True,
                    serialize=False,
                    verbose_name='Уникальный ключ'
                 )
                 ),
                ('role', models.TextField(null=True, verbose_name='Роль')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('film_work',
                 models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='movies.filmwork',
                    verbose_name='Кинопроизведение'
                 )
                 ),
                ('person',
                 models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='movies.person',
                    verbose_name='Человек'
                 )
                 ),
            ],
            options={
                'db_table': 'content"."person_film_work',
            },
        ),
        migrations.CreateModel(
            name='GenreFilmwork',
            fields=[
                ('id',
                 models.UUIDField(
                    default=uuid.uuid4,
                    editable=False,
                    primary_key=True,
                    serialize=False,
                    verbose_name='Уникальный ключ')
                 ),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('film_work',
                 models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='movies.filmwork',
                    verbose_name='Кинопроизведение'
                 )
                 ),
                ('genre',
                 models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='movies.genre',
                    verbose_name='Жанр'
                 )
                 ),
            ],
            options={
                'db_table': 'content"."genre_film_work',
            },
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(
                through='movies.GenreFilmwork',
                to='movies.genre',
                verbose_name='Жанр'
            ),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='person',
            field=models.ManyToManyField(
                through='movies.PersonFilmwork',
                to='movies.person',
                verbose_name='Человек'
            ),
        ),
    ]
