from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.traslados import router as traslado_router
from routes.choferes import router as choferes_router  # 👈 agregado

app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes cambiar esto por dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(traslado_router)
app.include_router(choferes_router)  # 👈 agregado

@app.get("/")
def root():
    return {"message": "API de Traslados funcionando correctamente"}
