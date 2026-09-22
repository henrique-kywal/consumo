
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repositories.abastecimento_repository import AbastecimentoRepository
from app.schemas.abastecimento_schema import (
    AbastecimentoCreate,
    AbastecimentoResponse,
)
from app.services.abastecimento_service import AbastecimentoService


router = APIRouter(
    prefix="/abastecimentos",
    tags=["Abastecimentos"]
)


@router.post("/", response_model=AbastecimentoResponse)
def criar_abastecimento(
    dados: AbastecimentoCreate,
    db: Session = Depends(get_db)
):
    repository = AbastecimentoRepository(db)
    service = AbastecimentoService(repository)

    resultado = service.criar(
        data=dados.data,
        quilometragem=dados.quilometragem,
        litros=dados.litros
    )

    abastecimento = resultado["abastecimento"]

    return {
        "id": abastecimento.id,
        "data": abastecimento.data,
        "quilometragem": abastecimento.quilometragem,
        "litros": abastecimento.litros,
        "quilometros_percorridos": resultado["quilometros_percorridos"],
        "consumo_km_l": resultado["consumo_km_l"]
    }

@router.get("/", response_model=list[AbastecimentoResponse])
def listar_abastecimentos(
    db: Session = Depends(get_db)
):
    repository = AbastecimentoRepository(db)
    service = AbastecimentoService(repository)

    abastecimentos = service.listar()

    return abastecimentos

@router.get("/{id}", response_model=AbastecimentoResponse)
def buscar_abastecimento_por_id(
    id: int,
    db: Session = Depends(get_db)
):
    repository = AbastecimentoRepository(db)
    service = AbastecimentoService(repository)

    return service.buscar_por_id(id)