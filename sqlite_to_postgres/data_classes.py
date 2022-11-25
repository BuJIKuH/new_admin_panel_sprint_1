from dataclasses import dataclass, asdict


@dataclass
class CurrentTable:

    @property
    def get_values_from_table(self):
        data = []
        for i in asdict(self).values():
            data.append(str(i))
        return '\t'.join(data)


@dataclass
class FilmWork(CurrentTable):
    __slots__ = (
        'id', 'title', 'description', 'creation_date',
        'file_path', 'rating', 'type', 'created_at', 'updated_at'
    )
    id: str
    title: str
    description: str
    creation_date: str
    file_path: str
    rating: float
    type: str
    created_at: str
    updated_at: str


@dataclass
class Genre(CurrentTable):
    __slots__ = (
        'id', 'name', 'description', 'created_at', 'updated_at'
    )
    id: str
    name: str
    description: str
    created_at: str
    updated_at: str


@dataclass
class Person(CurrentTable):
    __slots__ = (
        'id', 'full_name', 'created_at', 'updated_at'
    )
    id: str
    full_name: str
    created_at: str
    updated_at: str


@dataclass
class GenreFilmWork(CurrentTable):
    __slots__ = (
        'id', 'film_work_id', 'genre_id', 'created_at'
    )
    id: str
    film_work_id: str
    genre_id: str
    created_at: str


@dataclass
class PersonFilmWork(CurrentTable):
    __slots__ = (
        'id', 'film_work_id', 'person_id', 'role', 'created_at'
    )
    id: str
    film_work_id: str
    person_id: str
    role: str
    created_at: str
