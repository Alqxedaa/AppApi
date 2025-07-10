from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.traslados import router as traslado_router
from backend.routes.choferes import router as chofer_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringirlo si quieres más seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(traslado_router)
app.include_router(chofer_router)

@app.get("/")
def root():
    return {"message": "API de Traslados funcionando correctamente"}
