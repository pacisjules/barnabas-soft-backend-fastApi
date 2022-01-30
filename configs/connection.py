import databases
import sqlalchemy
from functools import lru_cache
from configs import dbinfo
from db.table import metadata

@lru_cache()
def db_config():
    return dbinfo.Setting()

def DATABASE_URL(
    connection: str = "postgresql",
    username: str   = "fspaqzexsyqjas",
    password: str   ="bcc2babd692e74cd177ec5ded7472078c0f683a40c40d8c12995e380f867be7d",
    host: str       = "ec2-54-208-139-247.compute-1.amazonaws.com",
    port: str       = "5432",
    database: str   = "ec2-54-208-139-247.compute-1.amazonaws.com"
):
    return str(connection+"://fspaqzexsyqjas:bcc2babd692e74cd177ec5ded7472078c0f683a40c40d8c12995e380f867be7d@ec2-54-208-139-247.compute-1.amazonaws.com:5432/dtaklrvatcmos")

database = databases.Database(DATABASE_URL())

engine = sqlalchemy.create_engine(
    DATABASE_URL()
)

metadata.create_all(engine)