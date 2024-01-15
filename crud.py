from sqlalchemy.orm import Session

import models
import schemas

###############
#CLIENTES
###############

def get_clientes(db: Session):
    return db.query(models.Clientes)


###############
#ENDERECOS
###############
def get_enderecos(db: Session):
    return db.query(models.Enderecos)

###############
#CARRINHOS
###############

def get_carrinhos(db: Session):
    return db.query(models.Carrinhos)


###############
#ITENS
###############

def get_itens(db: Session):
    return db.query(models.Itens)

###############
#Carrinho Itens
###############

def get_carrinho_itens(db: Session):
    return db.query(models.CarrinhoHasItem)