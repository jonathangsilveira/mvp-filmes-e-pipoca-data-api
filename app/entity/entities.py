from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from datetime import datetime
from typing import Optional

BaseEntity = declarative_base()

class WatchlistEntity(BaseEntity):
    __tablename__ = 'watchlist'

    id = Column('watchlist_id', Integer, 
                primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer, unique=True)
    insert_datetime = Column('insert_datetime', DateTime, nullable=False)
    
    def __init__(self, user_id: int, 
                 insert_date: datetime) -> None:
        """
        Cria um registro de lista filmes para assistir.

        Parâmetros:
            movie_id: ID do filme do TMDB API.
            user_id: ID do usuário.
            insert_date: Data e hora da criação do registro.
        """
        self.user_id = user_id
        self.insert_datetime = insert_date

class WatchlistItemEntity(BaseEntity):
    __tablename__ = 'watchlist_item'

    watchlist_id = Column('watchlist_id', Integer, primary_key=True)
    movie_id = Column('movie_id', Integer, primary_key=True)
    insert_datetime = Column('insert_datetime', DateTime, nullable=False)
    
    def __init__(self, watchlist_id: int, 
                 movie_id: int, insert_date: datetime) -> None:
        """
        Cria um registro de lista filmes para assistir.

        Parâmetros:
            movie_id: ID do filme do TMDB API.
            watchlist_id: ID do watchlist.
            insert_date: Data e hora da criação do registro.
        """
        self.watchlist_id = watchlist_id
        self.movie_id = movie_id
        self.insert_datetime = insert_date

class RatedMoviesEntity(BaseEntity):
    __tablename__ = 'rated_movies'

    user_id = Column('user_id', Integer, primary_key=True)
    movie_id = Column('movie_id', Integer, primary_key=True)
    rate_value = Column('rate_value', Integer, nullable=False)

    def __init__(self, movie_id: int, rate_value: int, 
                 user_id: int = 1) -> None:
        """
        Cria um registro de avaliação do filme.

        Parâmetros:
            movie_id: ID do filme do TMDB API.
            user_id: ID do usuário.
            rate_value: Valor da avaliação do filme. Valor entre 0 e 10.
        """
        self.user_id = user_id
        self.movie_id = movie_id
        self.rate_value = rate_value