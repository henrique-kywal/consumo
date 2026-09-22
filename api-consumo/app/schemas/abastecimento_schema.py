from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class AbastecimentoCreate(BaseModel):
    data: date
    quilometragem: float = Field(gt=0)
    litros: float = Field(gt=0)


class AbastecimentoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    data: date
    quilometragem: float
    litros: float
    quilometros_percorridos: float | None = None
    consumo_km_l: float | None = None