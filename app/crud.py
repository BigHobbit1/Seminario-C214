from sqlalchemy.orm import Session
import app.models as models, app.schemas as schemas

def criar_produto(db: Session, produto: schemas.ProdutoCreate):
    db_produto = models.Produto(**produto.dict())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

def listar_produtos(db: Session):
    return db.query(models.Produto).all()

def criar_venda(db: Session, venda: schemas.VendaCreate):
    produto = db.query(models.Produto).filter(models.Produto.id == venda.produto_id).first()
    if produto and produto.quantidade_estoque >= venda.quantidade:
        produto.quantidade_estoque -= venda.quantidade
        db_venda = models.Venda(**venda.dict())
        db.add(db_venda)
        db.commit()
        db.refresh(db_venda)
        return db_venda
    else:
        return None

def montar_computador(db: Session, computador: schemas.ComputadorCreate):
    novo_pc = models.Computador(nome=computador.nome)
    db.add(novo_pc)
    db.commit()
    db.refresh(novo_pc)

    for c in computador.componentes:
        produto = db.query(models.Produto).filter(models.Produto.id == c.produto_id).first()
        if not produto or produto.quantidade_estoque <= 0:
            continue
        produto.quantidade_estoque -= 1
        comp = models.ComputadorComponente(computador_id=novo_pc.id, produto_id=produto.id)
        db.add(comp)

    db.commit()
    return novo_pc
