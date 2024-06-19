from datetime import datetime
from typing import List

from app.entity import RatedMoviesEntity
from app.database import Session

async def rate_movie(movie_id: int, rate_value: int, user_id: int = 1) -> None:
    """
    Define nota para avaliação do filme.

    Parâmetros:
        movie_id: ID do filme do TMDB API.
        rate_value: Valor da avaliação do filme. Valor entre 0 e 10.
        user_id: ID do usuário.
    """
    session = Session()
    try:
        movies = session.query(RatedMoviesEntity). \
            filter(RatedMoviesEntity.user_id == user_id, RatedMoviesEntity.movie_id == movie_id). \
            all()
        if movies:
            rate = movies[0]
            rate.rate_value = rate_value
        else:
            rate = RatedMoviesEntity(movie_id=movie_id, user_id=user_id, 
                              rate_value=rate_value)
            session.add(rate)
        session.commit()
        session.close()
    except Exception as error:
        session.close()
        raise error
