import pytest
from pydantic import ValidationError

from app.schemas.abastecimento_schema import AbastecimentoCreate


def test_litros_deve_ser_maior_que_zero():
    with pytest.raises(ValidationError):
        AbastecimentoCreate(
            data="2026-09-21",
            quilometragem=52850,
            litros=0
        )

def test_quilometragem_deve_ser_maior_que_zero():
    with pytest.raises(ValidationError):
        AbastecimentoCreate(
            data="2026-09-21",
            quilometragem=0,
            litros=40
        )