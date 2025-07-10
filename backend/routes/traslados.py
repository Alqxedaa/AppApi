from fastapi import APIRouter, HTTPException
from backend.database import db

from backend.models import traslado_serializer

from bson import ObjectId

router = APIRouter()

@router.get("/traslados")
def obtener_traslados():
    traslados = db.traslados.find()
    return [traslado_serializer(t) for t in traslados]

@router.post("/traslados")
def crear_traslado(data: dict):
    result = db.traslados.insert_one(data)
    traslado = db.traslados.find_one({"_id": result.inserted_id})
    return traslado_serializer(traslado)

@router.put("/traslados/{id}")
def actualizar_traslado(id: str, data: dict):
    result = db.traslados.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Traslado no encontrado")
    traslado = db.traslados.find_one({"_id": ObjectId(id)})
    return traslado_serializer(traslado)

@router.delete("/traslados/{id}")
def eliminar_traslado(id: str):
    result = db.traslados.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Traslado eliminado"}
    raise HTTPException(status_code=404, detail="Traslado no encontrado")
