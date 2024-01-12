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