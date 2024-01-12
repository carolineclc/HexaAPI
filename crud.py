from sqlalchemy.orm import Session

import models
import schemas

###############
#CLIENTES
###############

def get_clientes(db: Session):
    return db.query(models.Clientes)
