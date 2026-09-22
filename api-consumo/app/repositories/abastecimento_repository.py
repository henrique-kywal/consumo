from sqlalchemy.orm import Session

from app.models.abastecimento import Abastecimento


class AbastecimentoRepository:

    def __init__(self, db: Session):
        self.db = db

    def criar(self, abastecimento: Abastecimento):
        self.db.add(abastecimento)
        self.db.commit()
        self.db.refresh(abastecimento)

        return abastecimento

    def buscar_anterior(self, quilometragem: float):
        return (
            self.db.query(Abastecimento)
            .filter(Abastecimento.quilometragem < quilometragem)
            .order_by(Abastecimento.quilometragem.desc())
            .first()
        )

    def listar(self):
        return (
            self.db.query(Abastecimento)
            .order_by(Abastecimento.quilometragem.asc())
            .all()
        )
    
    def buscar_por_id(self, id: int):
        return (
            self.db.query(Abastecimento)
            .filter(Abastecimento.id == id)
            .first()
        )