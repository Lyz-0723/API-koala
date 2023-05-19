from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine
from sshtunnel import SSHTunnelForwarder
import databases

# server = SSHTunnelForwarder(
#     ('122.116.234.117', 22),
#     ssh_username='ubuntu',
#     ssh_password='ubuntu server',
#     remote_bind_address=('localhost', 3306)
# )
#
# server.start()
# local_port = str(server.local_bind_port)

# DATABASE_URL = f"mysql+asyncmy://user:rKelsaoUa@localhost:{local_port}/Koala"
DATABASE_URL = f"mysql+asyncmy://user:rKelsaoUa@database-1.cbj0fmyu1hfa.us-east-1.rds.amazonaws.com:3306/Koala"
database = databases.Database(DATABASE_URL)

metadata = MetaData()
engine = create_async_engine(DATABASE_URL)
