from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.abastecimento import Abastecimento
from app.controllers.abastecimento_controller import (
    router as abastecimento_router
)


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Consumo",
    description="API para controle de abastecimentos e consumo de combustível",
    version="1.0.0"
)

app.include_router(abastecimento_router)


@app.get("/")
def root():
    return {
        "message": "API Consumo funcionando"
    }