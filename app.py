from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Configuración de la base de datos
DATABASE_URL = "sqlite:///./elements.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Elemento(Base):
    __tablename__ = "elementos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    simbolo = Column(String, index=True)
    numero_atomico = Column(Integer, index=True)
    peso_atomico = Column(String, index=True)

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/elementos/", response_model=list[Elemento])
def leer_elementos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    elementos = db.query(Elemento).offset(skip).limit(limit).all()
    return elementos

@app.get("/elementos/{elemento_id}", response_model=Elemento)
def leer_elemento(elemento_id: int, db: Session = Depends(get_db)):
    elemento = db.query(Elemento).filter(Elemento.id == elemento_id).first()
    if elemento is None:
        raise HTTPException(status_code=404, detail="Elemento no encontrado")
    return elemento

@app.post("/elementos/", response_model=Elemento)
def crear_elemento(elemento: Elemento, db: Session = Depends(get_db)):
    db.add(elemento)
    db.commit()
    db.refresh(elemento)
    return elemento

@app.put("/elementos/{elemento_id}", response_model=Elemento)
def actualizar_elemento(elemento_id: int, elemento_actualizado: Elemento, db: Session = Depends(get_db)):
    elemento = db.query(Elemento).filter(Elemento.id == elemento_id).first()
    if elemento is None:
        raise HTTPException(status_code=404, detail="Elemento no encontrado")
    elemento.nombre = elemento_actualizado.nombre
    elemento.simbolo = elemento_actualizado.simbolo
    elemento.numero_atomico = elemento_actualizado.numero_atomico
    elemento.peso_atomico = elemento_actualizado.peso_atomico
    db.commit()
    db.refresh(elemento)
    return elemento

@app.delete("/elementos/{elemento_id}", response_model=Elemento)
def eliminar_elemento(elemento_id: int, db: Session = Depends(get_db)):
    elemento = db.query(Elemento).filter(Elemento.id == elemento_id).first()
    if elemento is None:
        raise HTTPException(status_code=404, detail="Elemento no encontrado")
    db.delete(elemento)
    db.commit()
    return elemento

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
