from fastapi import APIRouter,HTTPException,status
from src.models import RifaCreateModel,RifaUpdateModel,RifaModel
from src.db.mongodb import db
from pymongo.errors import PyMongoError
from bson import ObjectId

router = APIRouter(prefix="/rifas")
rifas_collection = db['rifas']

@router.post("")
def create_rifa(rifaCreate: RifaCreateModel):
    rifa = RifaModel.from_create(rifaCreate)
    rifa_dict = rifa.model_dump(exclude={"id"})

    try:
        result = rifas_collection.insert_one(rifa_dict)
    except PyMongoError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao salvar no banco de dados: {str(e)}")
    
    return {"mensagem": "Rifa criada com sucesso!", "rifa": result.inserted_id.__str__()}

@router.get("")
def get_rifas():
    try:
        results = rifas_collection.find()
        rifas = [RifaModel(**result) for result in results]
    except PyMongoError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao buscar no banco de dados: {str(e)}")
    
    return {"mensagem": "Rifas encontradas com sucesso!", "rifas": rifas}

@router.get("/{id}")
def get_rifa(id: str):
    item_id_object = ObjectId(id)

    try:
        result = rifas_collection.find_one({'_id': item_id_object})
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rifa não encontrada")
        rifa = RifaModel(**result)

    except PyMongoError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao buscar no banco de dados: {str(e)}")
    
    return {"mensagem": "Rifa encontrada com sucesso!", "rifa": rifa}

@router.delete("/{id}")
def delete_rifa(id: str):
    item_id_object = ObjectId(id)

    try:
        result = rifas_collection.delete_one({'_id': item_id_object})  
        
        if result.deleted_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rifa não encontrada")
       
    except PyMongoError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao deletar no banco de dados: {str(e)}")
    
    return {"mensagem": "Rifa deletada com sucesso!","rifa": id}

@router.put("/{id}")
def update_rifa(id: str, rifaCreate: RifaUpdateModel):
    item_id_object = ObjectId(id)
    rifa = RifaModel.from_create(rifaCreate)
    rifa_dict = rifa.model_dump(exclude={"id"})

    try:
        result = rifas_collection.update_one({'_id': item_id_object}, {'$set': rifa_dict})
        
        if result.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rifa não encontrada")
    
    except PyMongoError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao atualizar no banco de dados: {str(e)}")
    
    return {"mensagem": "Rifa atualizada com sucesso!", "rifa": id}

