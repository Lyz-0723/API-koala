from sqlalchemy import create_engine, MetaData
from sshtunnel import SSHTunnelForwarder
import databases

server = SSHTunnelForwarder(
    ('122.116.234.117', 22),
    ssh_username='ubuntu',
    ssh_password='ubuntu server',
    remote_bind_address=('localhost', 3306)
)

server.start()
local_port = str(server.local_bind_port)

DATABASE_URL = f"mysql+pymysql://user:rKelsaoUa@localhost:{local_port}/Koala"
database = databases.Database(DATABASE_URL)

metadata = MetaData()
engine = create_engine(DATABASE_URL)
