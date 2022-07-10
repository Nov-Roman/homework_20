from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name='John')
    d2 = Director(id=2, name='Olivia')
    d3 = Director(id=3, name='Alex')

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2, d3])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.partially_update = MagicMock(return_value=Director(id=2))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


@pytest.fixture()
def genre():
    genre_dao = GenreDAO(None)

    comedy = Genre(id=1, name='comedy')
    drama = Genre(id=2, name='drama')
    horror = Genre(id=3, name='horror')

    genre_dao.get_one = MagicMock(return_value=comedy)
    genre_dao.get_all = MagicMock(return_value=[comedy, drama, horror])
    genre_dao.create = MagicMock(return_value=Genre(id=1))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


@pytest.fixture()
def movie():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='Фильм 1', description='описание 1', trailer='ссылка', year=2000,
                    rating=9.1, genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title='Фильм 2', description='описание 2', trailer='ссылка', year=2010,
                    rating=9.1, genre_id=2, director_id=2)
    movie_3 = Movie(id=3, title='Фильм 3', description='описание 3', trailer='ссылка', year=2020,
                    rating=9.1, genre_id=3, director_id=3)

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=1))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao
