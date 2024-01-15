from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ClientesBase(BaseModel):
    id_cliente: int
    nome: str = Field(
        title="Nome do membro",
        max_length=25,
        example="Joao"
    )
    sobrenome: Optional[str] = Field(
        title="Sobrenome do membro",
        max_length=25,
        example="Macedo"
    )
    instagram: Optional[str] = Field(
        title="Instagram do cliente para contato",
        example="@nome_sobrenome"
    )

    class Config:
        orm_mode = True

class EnderecosBase(BaseModel):
    id_endereco: int
    CEP: int = Field(
        title="CEP do endereco",
        example=112233
    )
    rua: Optional[str] = Field(
        title="Rua do endereco",
        max_length=25,
        example="av Brasil"
    )
    numero: Optional[int] = Field(
        title="Numero do endereco",
        example="123"
    )

    complemento: Optional[int] = Field(
        title="complemento do endereco",
        example="123"
    )

    class Config:
        orm_mode = True


class CarrinhosBase(BaseModel):
    id_carrinho: int
    pago: float = Field(
        example=1
    )
    entregue: float = Field(
        example=1
    )
    finalizado: float = Field(
        example=1
    )

    frete: float = Field(
        example=1.2
    )
    class Config:
        orm_mode = True

class ItensBase(BaseModel):
    id_item: int
    nome: str = Field(
        example="nome do set/item"
    )
    valor: float = Field(
        example=2.3
    )
    descricao: str = Field(
        example="descricao do set ou item"
    )
    class Config:
        orm_mode = True


class CarrinhosItensBase(BaseModel):
    id_carrinhoItem : int

    feito : int

    class Config:
        orm_mode = True
