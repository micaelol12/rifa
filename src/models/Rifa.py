from pydantic import BaseModel,Field,ConfigDict
from typing import List, Optional
import datetime

from .PyObjectId import PyObjectId
from .NumeroRifa import NumeroRifaModel
from .RifaCreate import RifaCreateModel

class RifaModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True,json_encoders={PyObjectId: str})

    id: Optional[PyObjectId] = Field(default=None,alias="_id", description="Unique identifier in mongo db")
    name: str
    description: str
    numeros: List[NumeroRifaModel] = []
    data_criacao: datetime.datetime

    @classmethod
    def from_create(cls, rifa_create: RifaCreateModel):
        return cls(
            name=rifa_create.name,
            description=rifa_create.description,
            numeros=[NumeroRifaModel.from_create(num) for num in rifa_create.numeros],
            data_criacao=datetime.datetime.now()
        )