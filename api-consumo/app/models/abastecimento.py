from sqlalchemy import Column, Date, Float, Integer

from app.database.database import Base


class Abastecimento(Base):
    __tablename__ = "abastecimentos"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date, nullable=False)
    quilometragem = Column(Float, nullable=False)
    litros = Column(Float, nullable=False)