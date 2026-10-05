from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.config import get_settings

settings = get_settings()

# Création du moteur SQLAlchemy
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,   # vérifie la connexion avant utilisation
    echo=False,           # mets True pour voir les requêtes SQL dans la console
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


class Base(DeclarativeBase):
    """Classe de base pour tous les modèles SQLAlchemy."""
    pass


def get_db():
    """
    Dépendance FastAPI : fournit une session de base de données
    et la ferme automatiquement à la fin de la requête.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()