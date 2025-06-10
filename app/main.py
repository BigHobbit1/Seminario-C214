from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import app.models as models, app.schemas as schemas, app.crud as crud
from app.database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/produtos/", response_model=schemas.ProdutoOut)
def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    return crud.criar_produto(db, produto)

@app.get("/estoque/", response_model=list[schemas.ProdutoOut])
def listar_estoque(db: Session = Depends(get_db)):
    return crud.listar_produtos(db)

@app.post("/vendas/")
def vender_produto(venda: schemas.VendaCreate, db: Session = Depends(get_db)):
    result = crud.criar_venda(db, venda)
    if not result:
        raise HTTPException(status_code=400, detail="Produto não encontrado ou estoque insuficiente")
    return {"mensagem": "Venda realizada com sucesso"}

@app.post("/computadores/montar")
def montar_computador(pc: schemas.ComputadorCreate, db: Session = Depends(get_db)):
    computador = crud.montar_computador(db, pc)
    return {"mensagem": "Computador montado com sucesso", "id": computador.id}
