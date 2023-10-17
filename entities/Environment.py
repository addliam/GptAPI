from dotenv import load_dotenv
load_dotenv()
import os

class Environment:
    """
    Carga la variable de entorno `ENVIRONMENT` que acepta valores de `development` o `production`
    """
    def __init__(self) -> None:
        POSIBLES = ["development", "production"]
        self.__ENVIRONMENT = os.getenv('ENVIRONMENT')
        if not self.__ENVIRONMENT in POSIBLES:
            raise Exception(f"El valor de la variable ENVIRONMENT debe ser {' o '.join(POSIBLES)}")
        
    def is_dev(self) -> bool:
        return self.__ENVIRONMENT == "development"
    
    def is_prod(self) -> bool:
        return self.__ENVIRONMENT == "production"