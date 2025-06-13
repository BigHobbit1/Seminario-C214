from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    tipo = Column(String)
    marca = Column(String)
    modelo = Column(String)
    preco = Column(Float)
    quantidade_estoque = Column(Integer)

class Venda(Base):
    __tablename__ = "vendas"
    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    quantidade = Column(Integer)
    tipo_venda = Column(String)  # "direta" ou "montado"
    data = Column(DateTime, default=datetime.utcnow)

class Computador(Base):
    __tablename__ = "computadores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    data_montagem = Column(DateTime, default=datetime.utcnow)
    componentes = relationship("ComputadorComponente", back_populates="computador")

class ComputadorComponente(Base):
    __tablename__ = "computador_componentes"
    id = Column(Integer, primary_key=True, index=True)
    computador_id = Column(Integer, ForeignKey("computadores.id"))
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    computador = relationship("Computador", back_populates="componentes")
