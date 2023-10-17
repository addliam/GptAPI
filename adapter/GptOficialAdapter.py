from dotenv import load_dotenv
load_dotenv()
from interface.GptInterface import GptInterface
from exceptions.NoEnvException import NoEnvException
from exceptions.MaxTokenException import MaxTokenException
import os
import openai

class GptOficialAdapter(GptInterface):
    
    def __init__(self):
        # iniciar GPT-3.5 API con el token
        self.__OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
        if not self.__OPENAI_API_KEY:
            raise NoEnvException("OPENAI_API_KEY")
        openai.api_key = self.__OPENAI_API_KEY

    def get_response(self, prompt_system: str, prompt_user:str, temperature: float) -> str:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt_system},
                {"role": "user", "content": prompt_user}],
            temperature=temperature)
        if completion.choices[0].finish_reason == "length":
            # means exceed 4096 tokens
            raise MaxTokenException
        gpt_response = completion.choices[0].message.content
        return gpt_response
    