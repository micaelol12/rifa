from pydantic import BaseModel
from typing import List

class RifaCreateModel(BaseModel):
    name: str
    description: str
    numeros: List[int]