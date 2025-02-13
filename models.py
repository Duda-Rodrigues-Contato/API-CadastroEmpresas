from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Empresa(Base):

    __tablename__ = "empresa" #Acho que consigo mudar pra "Empresa".

    id = Column(Integer, primary_key = True)
    nome = Column(String)
    cnpj = Column(String, unique = True)
    endereco = Column(String)
    email = Column(String)
    telefone = Column(String)

    obrigacaoacessoria = relationship("ObrigacaoAcessoria", back_populates = "empresas")



class ObrigacaoAcessoria(Base):

    __tablename__ = "ObrigacaoAcessoria" #Acho que consigo mudar pra "Obrigação Acessória".

    id = Column(Integer, primary_key = True)
    nome = Column(String)
    periodicidade = Column(String)
    empresa_id = Column(Integer, ForeignKey("obrigacaoacessoria"))

    empresas = relationship("Empresa", back_populates = "obrigacaoacessoria")
