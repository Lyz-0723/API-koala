from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    ('122.116.234.117', 22),
    ssh_username='ubuntu',
    ssh_password='ubuntu server',
    remote_bind_address=('localhost', 3306)
)

server.start()
local_port = str(server.local_bind_port)

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://user:rKelsaoUa@localhost:{local_port}/Koala"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
