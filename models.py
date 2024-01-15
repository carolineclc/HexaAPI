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
    carrinhos = relationship("Carrinhos", back_populates="clientes")


class Enderecos(Base):
    __tablename__ = "enderecos"

    id_endereco = Column(Integer, primary_key=True, index=True)
    CEP = Column(Integer, nullable=False, unique=True)
    rua = Column(String, nullable=False)
    numero = Column(Integer, nullable=False)
    complemento = Column(Integer, nullable=True)

    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"))

    clientes = relationship("Clientes", back_populates="enderecos")

class Carrinhos(Base):
    __tablename__ = "carrinhos"
    
    id_carrinho = Column(Integer, primary_key=True, index= True)
    valor = Column(Integer, nullable=False)
    pago = Column(Integer,nullable=False)
    entregue = Column(Integer,nullable=False)
    finalizado = Column(Integer,nullable=False)
    frete = Column(Integer,nullable=False)

    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"))
    clientes = relationship("Clientes", back_populates="carrinhos")
        
    
    carrinhos_tem_itens = relationship("CarrinhoHasItem", back_populates="carrinhos")

    
class Itens(Base):
    __tablename__ = "itens"
    
    id_item = Column(Integer, primary_key=True, index= True)
    nome = Column(String, nullable=False)
    valor = Column(Integer,nullable=False)
    descricao = Column(String,nullable=False)

    carrinhos_tem_itens = relationship("CarrinhoHasItem", back_populates="itens")

    

class CarrinhoHasItem(Base):
    __tablename__ = "carrinhos_tem_itens"
    
    id_carrinhoItem = Column(Integer, primary_key=True, index= True)
    feito = Column(Integer, nullable=False)
    lixado = Column(Integer, nullable=False)

    id_carrinho = Column(Integer, ForeignKey("carrinhos.id_carrinho"))
    id_item = Column(Integer, ForeignKey("itens.id_item"))

    carrinhos = relationship("Carrinhos", back_populates="carrinhos_tem_itens")
    itens = relationship("Itens", back_populates="carrinhos_tem_itens")