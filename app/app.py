from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, Response
from flask_cors import CORS

from app import *

info = Info(title="MVP Data API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

JSON_MIMETYPE = 'application/json'

@app.route('/api')
def swagger_doc():
    """Redireciona para visualização do estilo de documentação Swagger.
    """
    return redirect('/openapi/swagger')

@app.put(rule='/api/movie/rate/<int:movie_id>')
def put_rate_movie(path: RateMoviePathModel, body: RateMovieBodyModel) -> Response:
    """
    Rota para avaliação de filme.
    """
    try:
        rate_movie(movie_id=path.movie_id, rate_value=body.rate_value)
        return make_success_response(message='Filme avaliado com sucesso!')
    except Exception as error:
        return make_error_response(message='Erro ao avaliar filme!', code=404)
    
@app.post(rule='/api/watchlist/add')
def post_add_to_watchlist(body: AddToWatchlistBodyModel) -> Response:
    """
    Rota para adicionar uma filme na lista para assistir.
    """
    try:
        add_to_watchlist(movie_id=body.movie_id)
        return make_success_response(message='Filme adicionado com sucesso!')
    except TableIntegrityViolatedException as e:
        return make_error_response(message='Integridade da tabela violada!', code=409)
    except Exception as error:
        return make_error_response(message='Erro ao adicionar filme!', code=400)
    
@app.delete(rule='/api/watchlist/remove/<int:movie_id>')
def delete_remove_from_watchlist(path: RemoveFromWatchlistPathModel) -> Response:
    """
    Rota para adicionar uma filme na lista para assistir.
    """
    try:
        remove_from_watchlist(movie_id=path.movie_id)
        return make_success_response(message='Filme removido com sucesso!')
    except Exception as error:
        print(f'Erro ao remover filme: {str(error)}')
        return make_error_response(message='Erro ao remover filme', code=400)
    
def make_success_response(message: str) -> Response:
    """
    Produz uma resposta padrão de sucesso no formato JSON.
    """
    success = SuccessModel(message=message)
    return Response(
        mimetype=JSON_MIMETYPE,
        status=200,
        response=success.model_dump_json()
    )

def make_error_response(message: str, code: int) -> Response:
    """
    Produz uma resposta padrão de erro no formato JSON.
    """
    error = ErrorSchema(error_massage=message)
    return Response(
        mimetype=JSON_MIMETYPE,
        status=code,
        response=error.model_dump_json()
    )