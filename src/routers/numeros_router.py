
from fastapi import APIRouter,HTTPException,status
from src.models import NumeroRifaModel
from src.db.mongodb import db
from bson import ObjectId
from pymongo.errors import PyMongoError
from typing import List


router = APIRouter(prefix="/rifas/{id}/numeros")
rifas_collection = db['rifas']

@router.put("")
def update_rifa_numbers(id: str, numeros: List[NumeroRifaModel]):
    item_id_object = ObjectId(id)
    
    try:
        result = rifas_collection.update_one(
            {'_id': item_id_object},
            {'$set': {'numeros': [n.model_dump() for n in numeros]}}
        )
        
        if result.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rifa não encontrada")
    
    except PyMongoError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao atualizar números da rifa: {str(e)}")
    
    return {"mensagem": "Números da rifa atualizados com sucesso!"}

@router.get("")
def get_rifa_numbers(id: str): 
    item_id_object = ObjectId(id)
    
    try:
        result = rifas_collection.find_one({'_id': item_id_object}, {'numeros': 1})
        
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rifa não encontrada")
        
        numeros = result.get('numeros', [])
    
    except PyMongoError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao buscar números da rifa: {str(e)}")
    
    return {"mensagem": "Números da rifa encontrados com sucesso!", "numeros": numeros}

@router.put("/{numero}")
def update_numero_rifa(id: str, numero: int, numeroObjeto: NumeroRifaModel):
    item_id_object = ObjectId(id)
    
    try:
        result = rifas_collection.update_one(
            {'_id': item_id_object, 'numeros.numero': numero},
            {'$set': {'numeros.$': numeroObjeto.model_dump()}}
        )
        
        if result.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Número da rifa não encontrado")
    
    except PyMongoError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao atualizar número da rifa: {str(e)}")
    
    return {"mensagem": "Número da rifa atualizado com sucesso!"}