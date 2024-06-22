from app.schema.schemas import RateMoviePathModel, RateMovieBodyModel
from app.schema.schemas import AddToWatchlistPathModel, RemoveFromWatchlistPathModel, WatchlistModel, GetWatchlistQueryModel, WatchlistCreatedModel
from app.schema.schemas import SuccessModel, ErrorModel

from app.controller.rate_controller import rate_movie
from app.controller.watchlist_controller import add_to_watchlist, remove_from_watchlist, get_watchlist_movies, create_watchlist

from app.business.exceptions import TableIntegrityViolatedException, RecordNotFoundException