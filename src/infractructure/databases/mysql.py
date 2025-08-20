# Example engine factory for MYSQL
from .base import init_engine
def get_engine(url: str = "mysql+pymysql://user:password@localhost:3306/ims"):
    return init_engine(url)