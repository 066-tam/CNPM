from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from contextlib import contextmanager

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False)

def init_engine(database_url: str):
    engine = create_engine(database_url, pool_pre_ping=True, future=True)
    SessionLocal.configure(bind=engine)
    return engine

@contextmanager
def db_session():
    from .base import SessionLocal
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()