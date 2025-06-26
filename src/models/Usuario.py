from pydantic import BaseModel

class UsuarioModel(BaseModel):
    nome: str
    email: str
    telefone: str
