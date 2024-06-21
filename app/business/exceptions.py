

class TableIntegrityViolatedException(Exception):
    """
    Exceção lançada quando a integridade da tabela é violada
    """

class RecordNotFoundException(Exception):
    """
    Exceção lançada quando não é encontrado registro na base de dados.
    """