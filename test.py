from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import psycopg2
from sqlalchemy.ext.asyncio import create_async_engine

conn = psycopg2.connect(user='postgres', password='postgres', host='localhost', port='5432')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()

request = "postgresql+asyncpg://postgres:postgres@postgres:5432/memes_data"
engine = create_async_engine(request)
print(engine)