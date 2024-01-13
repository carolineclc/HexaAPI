from fastapi import Depends,FastAPI, Request, status, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from database import SessionLocal, engine
import crud
import schemas
import models
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/clientes/", response_model=list[schemas.ClientesBase], status_code=200, tags=["Clientes"], 
         description="Retorna a lista de todos os membros, com seus respectivos atributos")
async def get_clientes(db : Session = Depends(get_db)):
    clientes = crud.get_clientes(db)
    return clientes

@app.get("/enderecos/", response_model=list[schemas.EnderecosBase], status_code=200, tags=["Enderecos"], 
         description="Retorna a lista de todos os enderecos, com seus respectivos atributos")
async def get_enderecos(db : Session = Depends(get_db)):
    enderecos = crud.get_enderecos(db)
    return enderecos