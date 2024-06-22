from datetime import datetime
from typing import List
from sqlalchemy.exc import IntegrityError

from app.business.exceptions import TableIntegrityViolatedException, RecordNotFoundException

from app.schema.schemas import WatchlistModel, WatchlistCreatedModel

from app.entity import WatchlistEntity, WatchlistItemEntity

from app.database import Session

def create_watchlist(user_id: int = 1) -> WatchlistCreatedModel:
    """
    Cria um registro da lista.

    Parâmetro:
        user_id: ID do usuário.
    """
    session = Session()
    try:
        watchlist = WatchlistEntity(
            user_id=user_id, 
            insert_date=datetime.now()
        )
        session.add(watchlist)
        session.commit()
        return WatchlistCreatedModel(watchlist_id=watchlist.id)
    except IntegrityError:
        raise TableIntegrityViolatedException()
    finally:
        session.close()

def add_to_watchlist(movie_id: int, watchlist_id: int) -> None:
    """
    Adiciona o filme na lista para assistir do usuário.

    Parâmetros:
        movie_id: ID do filme do TMDB API.
        watchlist_id: ID do watchlist.
    """
    session = Session()
    try:
        watchlist_item = WatchlistItemEntity(
            watchlist_id=watchlist_id,
            movie_id=movie_id, 
            insert_date=datetime.now()
        )
        session.add(watchlist_item)
        session.commit()
    except IntegrityError:
        raise TableIntegrityViolatedException()
    finally:
        session.close()
    
def remove_from_watchlist(movie_id: int, watchlist_id: int) -> None:
    """
    Remover o filme na lista para assistir do usuário.

    Parâmetros:
        movie_id: ID do filme do TMDB API.
        watchlist_id: ID do watchlist.
    """
    session = Session()
    try:
        movies = session.query(WatchlistItemEntity). \
            filter(
                WatchlistItemEntity.watchlist_id == watchlist_id, 
                WatchlistItemEntity.movie_id == movie_id
            ).all()
        if movies:
            session.delete(movies[0])
            session.commit()
        session.close()
    except Exception as error:
        session.close()
        raise error

def get_watchlist_movies(watchlist_id: int) -> WatchlistModel:
    """
    Adiciona o filme na lista para assistir do usuário.

    Parâmetros:
        watchlist_id: ID do watchlist.
    """
    session = Session()
    try:
        watchlist = session.get(WatchlistEntity, watchlist_id)
        if not watchlist:
            raise RecordNotFoundException()
        items = session.query(WatchlistItemEntity). \
            filter(WatchlistItemEntity.watchlist_id == watchlist_id). \
            order_by(WatchlistItemEntity.insert_datetime). \
            all()
        return WatchlistModel(
            watchlist_id=watchlist_id,
            movie_ids=[item.movie_id for item in items]
        )
    finally:
        session.close()
