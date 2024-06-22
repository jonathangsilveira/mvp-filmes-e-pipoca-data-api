from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, Response
from flask_cors import CORS
from pydantic import BaseModel

from app import *

info = Info(title="MVP Data API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

rate_tag = Tag(name='Avaliação de filmes', 
               description='Avaliar um filme atribuindo uma nota de 0 a 10')
watchlist_tag = Tag(name='Lista para assistir depois', 
                    description='Adição, remoção e visualização de lista com filmes.')

JSON_MIMETYPE = 'application/json'

@app.route('/api')
def swagger_doc():
    """Redireciona para visualização do estilo de documentação Swagger.
    """
    return redirect('/openapi/swagger')

@app.put(rule='/api/movie/rate/<int:movie_id>', tags=[rate_tag], 
         responses={200: SuccessModel, 400: ErrorModel})
def put_rate_movie(path: RateMoviePathModel, body: RateMovieBodyModel) -> Response:
    """
    Rota para avaliação de filme.
    """
    try:
        rate_movie(movie_id=path.movie_id, rate_value=body.rate_value)
        return make_success_response(message='Filme avaliado com sucesso!')
    except Exception as error:
        return make_error_response(message='Erro ao avaliar filme!', code=404)
    
@app.post(rule='/api/watchlist/<int:watchlist_id>/add', tags=[watchlist_tag], 
          responses={200: SuccessModel, 400: ErrorModel, 409: ErrorModel})
def post_add_to_watchlist(body: AddToWatchlistBodyModel) -> Response:
    """
    Rota para adicionar uma filme na lista para assistir.
    """
    try:
        add_to_watchlist(movie_id=body.movie_id)
        return make_success_response(message='Filme adicionado com sucesso!')
    except TableIntegrityViolatedException:
        return make_error_response(message='Integridade da tabela violada!', code=409)
    except Exception:
        return make_error_response(message='Erro ao adicionar filme!', code=400)
    
@app.delete(rule='/api/watchlist/<int:watchlist_id>/remove/<int:movie_id>', tags=[watchlist_tag], 
            responses={200: SuccessModel, 400: ErrorModel})
def delete_remove_from_watchlist(path: RemoveFromWatchlistPathModel) -> Response:
    """
    Rota para adicionar uma filme na lista para assistir.
    """
    try:
        remove_from_watchlist(movie_id=path.movie_id)
        return make_success_response(message='Filme removido com sucesso!')
    except Exception:
        return make_error_response(message='Erro ao remover filme', code=400)
    
@app.get(rule='/api/watchlist', tags=[watchlist_tag], 
         responses={200: WatchlistModel, 400: ErrorModel, 404: ErrorModel})
def get_watchlist(query: GetWatchlistQueryModel) -> Response:
    """
    Rota para recuperar uma lista para assistir.
    """
    try:
        watchlist = get_watchlist_movies(query.watchlist_id)
        return make_json_response(watchlist)
    except RecordNotFoundException:
        return make_error_response(
            message='Lista não encontrada!',
            code=404
        )
    except Exception:
        return make_error_response(
            message='Erro ao recuperar lista para assistir!',
            code=400
        )
    
def make_success_response(message: str) -> Response:
    """
    Produz uma resposta padrão de sucesso no formato JSON.

    Parâmetro:
        message: Mensagem de sucesso.
    """
    success = SuccessModel(message=message)
    return make_json_response(model=success)

def make_error_response(message: str, code: int) -> Response:
    """
    Produz uma resposta padrão de erro no formato JSON.

    Parâmetro:
        message: Mensagem de sucesso.
        code: Código HTTP de erro.
    """
    error = ErrorModel(error_massage=message)
    return make_json_response(
        model=error,
        code=code
    )

def make_json_response(model: BaseModel, code: int = 200) -> Response:
    """
    Produz uma resposta padrão de erro no formato JSON.

    Parâmetros:
        model: Modelo que será convertido em JSON.
        code: Código HTTP de erro.
    """
    return Response(
        mimetype=JSON_MIMETYPE,
        status=code,
        response=model.model_dump_json()
    )