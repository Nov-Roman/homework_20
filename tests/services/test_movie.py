import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie):
        self.movie_service = MovieService(dao=movie)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "id": 1,
            "title": "new_title",
            "description": "new_description",
            "trailer": "new_trailer",
            "year": 2000,
            "rating": 7.0,
            "genre_id": 2,
            "director_id": 2
        }
        movie = self.movie_service.create(movie_d)

        assert movie.id is not None

    def test_update(self):
        movie_d = {
            "id": 2,
            "title": "new_title2",
            "description": "new_description2",
            "trailer": "new_trailer2",
            "year": 2002,
            "rating": 9.0,
            "genre_id": 3,
            "director_id": 3
        }
        self.movie_service.update(movie_d)

    def test_delete(self):
        self.movie_service.delete(1)
