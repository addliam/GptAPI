from abc import (
    ABCMeta,
    abstractmethod
)

class GptInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_response(self, prompt_system: str, prompt_user:str, temperature: float):
        """
        Interface para posterior implementacion.

        Parameters:
            prompt_system (str): El prompt de sistema. Admite cadena vacia de texto.
            prompt_user (int): El prompt de usuario.
            temperature (str): Temperatura es el grado creatividad y diversidad de texto generado [0-1].
        """
        pass