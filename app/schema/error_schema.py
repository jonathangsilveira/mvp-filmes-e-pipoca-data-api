from typing import Optional
from pydantic import BaseModel

class ErroSchema(BaseModel):
    """
    Define contrato para exibição de erros da API.
    """
    mensagem: str = "Erro ao adicionar filme na watchlist!"