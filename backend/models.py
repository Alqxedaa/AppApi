from pydantic import BaseModel

# MODELOS PARA LOGIN
class LoginInput(BaseModel):
    id: str
    password: str

class ChoferOutput(BaseModel):
    id: str
    nombre: str

# SERIALIZADOR DE TRASLADOS
def traslado_serializer(traslado) -> dict:
    return {
        "id": str(traslado["_id"]),
        "paciente": traslado["paciente"],
        "direccion": traslado["direccion"],
        "hora": traslado["hora"],
        "chofer_id": traslado.get("chofer_id", ""),
        "estado": traslado.get("estado", "pendiente")
    }
