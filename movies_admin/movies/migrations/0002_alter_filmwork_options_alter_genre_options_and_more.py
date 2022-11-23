# Generated by Django 4.1.3 on 2022-11-23 15:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filmwork',
            options={'verbose_name': 'film work', 'verbose_name_plural': 'films work'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'genre', 'verbose_name_plural': 'genres'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'person', 'verbose_name_plural': 'persons'},
        ),
        migrations.AddField(
            model_name='filmwork',
            name='certificate',
            field=models.CharField(blank=True, max_length=512, verbose_name='certificate'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='file_path',
            field=models.FileField(blank=True, null=True, upload_to='movies/', verbose_name='file'),
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.TextField(choices=[('male', 'male'), ('female', 'female')], null=True, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='creation_date',
            field=models.DateField(blank=True, verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(through='movies.GenreFilmwork', to='movies.genre', verbose_name='genres'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique key'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='person',
            field=models.ManyToManyField(through='movies.PersonFilmwork', to='movies.person', verbose_name='person'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='rating',
            field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='rating'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='type',
            field=models.CharField(blank=True, choices=[('movies', 'movies'), ('tv_show', 'tv_show')], default='movies', max_length=20, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique key'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='genrefilmwork',
            name='film_work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork', verbose_name='film work'),
        ),
        migrations.AlterField(
            model_name='genrefilmwork',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre', verbose_name='genre'),
        ),
        migrations.AlterField(
            model_name='genrefilmwork',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique key'),
        ),
        migrations.AlterField(
            model_name='person',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='person',
            name='full_name',
            field=models.CharField(max_length=150, verbose_name='full name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique key'),
        ),
        migrations.AlterField(
            model_name='person',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='personfilmwork',
            name='film_work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork', verbose_name='film work'),
        ),
        migrations.AlterField(
            model_name='personfilmwork',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='unique key'),
        ),
        migrations.AlterField(
            model_name='personfilmwork',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person', verbose_name='person'),
        ),
        migrations.AlterField(
            model_name='personfilmwork',
            name='role',
            field=models.TextField(null=True, verbose_name='role'),
        ),
    ]