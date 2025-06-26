from models.classes.NumeroRifa import NumeroRifa
from typing import List
import datetime

class Rifa():
    def __init__(self, id, name, description):
        self.id:str = id
        self.name:str = name
        self.description:str = description
        self.numeros:List[NumeroRifa] = []
        self.data_criacao:datetime = datetime.datetime.now()

    def __str__(self):
        return f"Rifa(id={self.id}, name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})"