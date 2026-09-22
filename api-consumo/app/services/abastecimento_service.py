from app.models.abastecimento import Abastecimento
from app.repositories.abastecimento_repository import AbastecimentoRepository
from fastapi import HTTPException

class AbastecimentoService:

    def __init__(self, repository: AbastecimentoRepository):
        self.repository = repository


    def criar(self, data, quilometragem, litros):
        abastecimentos = self.repository.listar()

        if abastecimentos:
            ultimo_abastecimento = abastecimentos[-1]

            if quilometragem <= ultimo_abastecimento.quilometragem:
                raise HTTPException(
                    status_code=400,
                    detail=(
                        "A quilometragem deve ser maior "
                        "que a do último abastecimento."
                    )
                )

        abastecimento_anterior = (
            self.repository.buscar_anterior(quilometragem)
        )

        abastecimento = Abastecimento(
            data=data,
            quilometragem=quilometragem,
            litros=litros
        )

        quilometros_percorridos = None
        consumo_km_l = None

        if abastecimento_anterior:
            quilometros_percorridos = (
                quilometragem - abastecimento_anterior.quilometragem
            )

            consumo_km_l = quilometros_percorridos / litros

        abastecimento = self.repository.criar(abastecimento)

        return {
            "abastecimento": abastecimento,
            "quilometros_percorridos": quilometros_percorridos,
            "consumo_km_l": consumo_km_l
        }
   
    def listar(self):
        abastecimentos = self.repository.listar()

        resultado = []

        abastecimento_anterior = None

        for abastecimento in abastecimentos:
            quilometros_percorridos = None
            consumo_km_l = None

            if (
                abastecimento_anterior
                and abastecimento.quilometragem
                > abastecimento_anterior.quilometragem
            ):
                quilometros_percorridos = (
                    abastecimento.quilometragem
                    - abastecimento_anterior.quilometragem
                )

                consumo_km_l = (
                    quilometros_percorridos / abastecimento.litros
                )

            resultado.append({
                "id": abastecimento.id,
                "data": abastecimento.data,
                "quilometragem": abastecimento.quilometragem,
                "litros": abastecimento.litros,
                "quilometros_percorridos": quilometros_percorridos,
                "consumo_km_l": consumo_km_l
            })

            abastecimento_anterior = abastecimento

        return resultado

    def buscar_por_id(self, id: int):
        abastecimento = self.repository.buscar_por_id(id)

        if not abastecimento:
            raise HTTPException(
                status_code=404,
                detail="Abastecimento não encontrado."
            )

        return abastecimento