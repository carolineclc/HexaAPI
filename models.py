from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, BigInteger
from sqlalchemy.orm import relationship

from database import Base


class Clientes(Base):
    __tablename__ = "clientes"

    id_cliente = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    sobrenome = Column(String, nullable=False)
    instagram = Column (String, nullable= False)
    CPF = Column (Integer, nullable= False, unique= True)