-- создаем новую схему, если ее нет
CREATE SCHEMA IF NOT EXISTS content;

-- выбираем роль по умолчанию 'content'
ALTER ROLE app SET search_path TO content,public;

-- создаем объект "Произведения", предварительно проверяя был ли он создан ранее
    -- в объекте описываются поля: уникальный ключ, заголовок фильма, описание
    -- фильма, дата создания фильма, рейтинг, тип, дата создания записи и дата
    -- изменения записи.
CREATE TABLE IF NOT EXISTS film_work (
    id uuid PRIMARY KEY,
    title VARCHAR(30) NOT NULL,
    description TEXT,
    creation_date DATE,
    rating FLOAT,
    type TEXT not null,
    created timestamp with time zone,
    modified timestamp with time zone
);

-- создаем объект "Жанр", предварительно проверяя был ли он создан ранее
    -- в объекте описываются поля: уникальный ключ, название, описание,  дата
    -- создания записи и дата изменения записи.
CREATE TABLE IF NOT EXISTS genre (
    id uuid PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    description TEXT,
    created timestamp with time zone,
    modified timestamp with time zone
);

-- создаем объект "Люди", предварительно проверяя был ли он создан ранее
    -- в объекте описываются поля: уникальный ключ, полное имя,  дата создания
    --  записи и дата изменения записи.
CREATE TABLE IF NOT EXISTS person (
    id uuid PRIMARY KEY,
    full_name VARCHAR(40) NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
);

-- создаем связанный объект "Люди" и "Произведения", предварительно проверяя
    -- был ли он создан ранее;
    -- в объекте описываются поля: уникальный ключ, отношение к уникальному
    -- ключу в объекте "Люди", отношение к уникальному ключу в объекте
    -- "Произведения", роль, дата создания записи.
CREATE TABLE IF NOT EXISTS person_film_work (
    id uuid PRIMARY KEY,
    person_id uuid NOT NULL,
    film_work_id uuid NOT NULL,
    FOREIGN KEY (film_work_id)
        REFERENCES film_work (id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (person_id)
        REFERENCES person (id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    role VARCHAR(30),
    created timestamp with time zone
    );

-- создаем связанный объект "Жанр"  и "Произведения", предварительно проверяя
    -- был ли он создан ранее
    -- в объекте описываются поля: уникальный ключ, отношение к уникальному
    -- ключу в объекте "Жанр", отношение к уникальному ключу в объекте
    -- "Произведения", дата создания записи.
CREATE TABLE  IF NOT EXISTS genre_film_work (
	id uuid PRIMARY KEY,
	genre_id uuid NOT NULL,
    film_work_id uuid NOT NULL,
	FOREIGN KEY (genre_id)
        REFERENCES genre(id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(film_work_id)
	    REFERENCES film_work(id)
	    ON DELETE CASCADE ON UPDATE CASCADE,
	created timestamp with time zone
	);


-- создаем уникальный индекс для поиска по связанному объекту
-- "Жанр"  и "Произведения" по полям (film_work_id, genre_id).
CREATE UNIQUE INDEX genre_film_work_idx
    ON genre_film_work(film_work_id, genre_id);

-- создаем уникальный индекс для поиска по связанному объекту
-- "Люди" и "Произведения" по полям (role, person_id).
CREATE UNIQUE INDEX person_film_work_idx
    ON person_film_work (role, person_id);


