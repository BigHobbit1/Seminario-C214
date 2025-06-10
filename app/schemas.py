from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ProdutoBase(BaseModel):
    nome: str
    tipo: str
    marca: str
    modelo: str
    preco: float
    quantidade_estoque: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoOut(ProdutoBase):
    id: int

    class Config:
        orm_mode = True

class VendaCreate(BaseModel):
    produto_id: int
    quantidade: int
    tipo_venda: str

class ComputadorComponenteIn(BaseModel):
    produto_id: int

class ComputadorCreate(BaseModel):
    nome: str
    componentes: List[ComputadorComponenteIn]

class ComputadorOut(BaseModel):
    id: int
    nome: str
    data_montagem: datetime
