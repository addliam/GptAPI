class NoEnvException(Exception):
    """
    Excepcion levantada cuando una variable de entorno no esta presente.

    Attributes:
        name (str): El nombre de la variable de entorno.
    """

    def __init__(self, name="") -> None:
        message = f"Variable de entorno no establecida. {name}"
        super().__init__(message)