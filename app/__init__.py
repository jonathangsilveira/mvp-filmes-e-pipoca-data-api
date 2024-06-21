from app.schema.schemas import RateMoviePathModel, RateMovieBodyModel
from app.schema.schemas import AddToWatchlistBodyModel, RemoveFromWatchlistPathModel, WatchlistModel
from app.schema.schemas import SuccessModel, ErrorSchema

from app.controller.rate_controller import rate_movie
from app.controller.watchlist_controller import add_to_watchlist, remove_from_watchlist, get_watchlist_movies

from app.business.exceptions import TableIntegrityViolatedException, RecordNotFoundException