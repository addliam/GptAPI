from fastapi import FastAPI
from adapter import GptOficialAdapter
from entities import Environment
from entities import GptBody

app = FastAPI()

# instanciar objetos
gpt_oficial = GptOficialAdapter()
env = Environment()

@app.get("/")
async def root():
    return {"status": "Alive"}

@app.post("/chat")
async def chat_gpt(gpt_body: GptBody):
    if env.is_prod():    
        response = gpt_oficial.get_response(
            prompt_system=gpt_body.prompt_system,
            prompt_user=gpt_body.prompt_user,
            temperature=gpt_body.temperature)
        return {"answer": response}
    else:
        # Aca insertar codigo de inicializacion de GptNoOficial y retornar igual `{"answer": response}`
        return {"answer": "No implementado"}
        
# uvicorn main:app --reload