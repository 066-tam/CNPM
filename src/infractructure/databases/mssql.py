# Example engine factory for MSSQL
from .base import init_engine
def get_engine(url: str = "mssql+pyodbc://user:password@localhost:1433/ims?driver=ODBC+Driver+17+for+SQL+Server"):
    return init_engine(url)