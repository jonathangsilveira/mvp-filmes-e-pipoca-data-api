from datetime import datetime
from typing import List
from sqlalchemy.exc import IntegrityError

from app.business.exceptions import TableIntegrityViolatedException, RecordNotFoundException

from app.entity import WatchlistEntity

from app.database import Session

def add_to_watchlist(movie_id: int, user_id: int = 1) -> None:
    """
    Adiciona o filme na lista para assistir do usuário.

    Parâmetros:
        movie_id: ID do filme do TMDB API.
        user_id: ID do usuário.
    """
    session = Session()
    try:
        watchlist = WatchlistEntity(
            movie_id=movie_id, 
            user_id=user_id, 
            insert_date=datetime.now()
        )
        session.add(watchlist)
        session.commit()
    except IntegrityError as e:
        raise TableIntegrityViolatedException()
    finally:
        session.close()
    
def remove_from_watchlist(movie_id: int, user_id: int = 1) -> None:
    """
    Remover o filme na lista para assistir do usuário.

    Parâmetros:
        movie_id: ID do filme do TMDB API.
        user_id: ID do usuário.
    """
    session = Session()
    try:
        movies = session.query(WatchlistEntity).filter(WatchlistEntity.user_id == user_id, WatchlistEntity.movie_id == movie_id).all()
        if movies:
            session.delete(movies[0])
            session.commit()
        session.close()
    except Exception as error:
        session.close()
        raise error

def get_watchlist_movies(user_id: int = 1) -> List[int]:
    """
    Adiciona o filme na lista para assistir do usuário.

    Parâmetros:
        user_id: ID do usuário.
    """
    session = Session()
    try:
        watchlist = session.query(WatchlistEntity). \
            filter(WatchlistEntity.user_id == user_id). \
            order_by(WatchlistEntity.insert_datetime). \
            all()
        if not watchlist:
            raise RecordNotFoundException()
        movies_id = [item.movie_id for item in watchlist]
        return movies_id
    finally:
        session.close()
