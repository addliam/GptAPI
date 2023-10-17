from pydantic import BaseModel

class GptBody(BaseModel):
    # prompt de usuario es obligatorio
    prompt_system: str | None = None
    prompt_user: str
    temperature: float | None = None
