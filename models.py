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

    enderecos = relationship("Enderecos", back_populates="clientes")


class Enderecos(Base):
    __tablename__ = "enderecos"

    id_endereco = Column(Integer, primary_key=True, index=True)
    CEP = Column(Integer, nullable=False, unique=True)
    rua = Column(String, nullable=False)
    numero = Column(Integer, nullable=False)
    complemento = Column(Integer, nullable=True)

    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"))

    clientes = relationship("Clientes", back_populates="enderecos")
       