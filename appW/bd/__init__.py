"""
Базовый __init__ файл подгружающий все переменные, сессии и зависимости SQLAlchemy, Minio
"""

from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from appW.bd.db_connect import db_conn, create_db_tables
from appW.bd.schemas import Memes_model, met, Table_MODEL

create_db_tables()
dbI = db_conn()
connI = dbI.engine
Declar_Memes = Table_MODEL
sessionI = dbI.Session_db
async def get_session() -> AsyncGenerator[AsyncSession, None]:
	async with sessionI() as session:
		yield session
