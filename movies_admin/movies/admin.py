from django.contrib import admin
from .models import Genre, GenreFilmWork, FilmWork, PersonFilmWork, Person


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmWork


class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmWork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(FilmWork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline, PersonFilmworkInline)
    list_display = (
        'title', 'type', 'creation_date', 'rating')
    list_filter = ('type',)
    search_fields = ('title', 'description', 'id', 'type')
