import pytest
from datetime import date
from fastapi import HTTPException

from app.services.abastecimento_service import AbastecimentoService


class RepositoryFake:

    def __init__(self):
        self.abastecimentos = []

    def listar(self):
        return self.abastecimentos

    def buscar_anterior(self, quilometragem):
        if not self.abastecimentos:
            return None

        return self.abastecimentos[-1]

    def criar(self, abastecimento):
        abastecimento.id = len(self.abastecimentos) + 1
        self.abastecimentos.append(abastecimento)

        return abastecimento


def test_calcular_consumo():
    repository = RepositoryFake()

    service = AbastecimentoService(repository)

    primeiro = service.criar(
        data=date(2026, 9, 19),
        quilometragem=52350,
        litros=40
    )

    segundo = service.criar(
        data=date(2026, 9, 21),
        quilometragem=52850,
        litros=40
    )

    assert segundo["quilometros_percorridos"] == 500
    assert segundo["consumo_km_l"] == 12.5


def test_nao_permitir_quilometragem_menor_ou_igual():
    repository = RepositoryFake()

    service = AbastecimentoService(repository)

    service.criar(
        data=date(2026, 9, 19),
        quilometragem=52350,
        litros=40
    )

    with pytest.raises(HTTPException) as erro:
        service.criar(
            data=date(2026, 9, 21),
            quilometragem=52350,
            litros=40
        )

    assert erro.value.status_code == 400
    assert "quilometragem deve ser maior" in erro.value.detail