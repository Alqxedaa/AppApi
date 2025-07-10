from fastapi import APIRouter, HTTPException, Body
from backend.models import LoginInput, ChoferOutput
from backend.database import db

from backend.models import traslado_serializer


router = APIRouter()

# Ruta de login
@router.post("/login", response_model=ChoferOutput)
def login(data: LoginInput):
    chofer = db.choferes.find_one({
        "id": data.id,
        "password": data.password
    })
    if chofer:
        return {
            "id": chofer["id"],
            "nombre": chofer["nombre"]
        }
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")

# Ruta para crear un nuevo chofer
@router.post("/choferes")
def crear_chofer(data: dict = Body(...)):
    if db.choferes.find_one({"id": data["id"]}):
        raise HTTPException(status_code=400, detail="El ID del chofer ya existe")

    nuevo_chofer = {
        "id": data["id"],
        "nombre": data["nombre"],
        "password": data["password"]
    }
    db.choferes.insert_one(nuevo_chofer)
    return {"message": "Chofer creado exitosamente"}

# Ruta para obtener todos los choferes
@router.get("/choferes")
def obtener_choferes():
    choferes = db.choferes.find()
    return [{"id": c["id"], "nombre": c["nombre"]} for c in choferes]

# Ruta para obtener traslados asignados a un chofer
@router.get("/choferes/{id}/traslados")
def obtener_traslados_por_chofer(id: str):
    traslados = db.traslados.find({"chofer_id": id})
    return [traslado_serializer(t) for t in traslados]
