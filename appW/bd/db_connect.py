"""

Файл проверок на наличие в Postgresql нужной базы данных и таблицы, он же раздает файл сессии

"""

import psycopg2
from sqlalchemy import create_engine
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from appW.bd.schemas import Base

class db_conn:
	"""
	Ассинхронное подключение к Postgresql
	"""
	def __init__(self):
		self.create_enginers()
	def create_enginers(self):
		"""Функция подключения"""
		request = "postgresql+asyncpg://postgres:postgres@localhost/memes_data"
		self.engine = create_async_engine(request)
		self.get_session()
		print('[connection is successful]')
	def get_session(self):
		"""Раздача сессии"""
		self.Session_db = sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)

class create_db_tables():
	"""Синхронное создание базы данных и таблицы"""
	def __init__(self):
		self.creators()
	def creators(self):
		"""Синхронное подключение к Postgresql для создания таблицы и базы данных, с проверкой на наличие и того и другого"""
		conn = psycopg2.connect(user='postgres', password='postgres', host='localhost', port='5432')
		conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
		cur = conn.cursor()
		try:
			cur.execute('create database Memes_data')
			self.creators()
		except:
			print('[The database exists]')
		conn.close()

		# ||||||||||||

		request = "postgresql+psycopg2://postgres:postgres@localhost/memes_data"
		self.engine = create_engine(request)
		try:
			self.create_table()
		except:
			print('Table status: YES')
	def create_table(self):
		"""Создание таблицы"""
		print('Table_create...')
		Base.metadata.tables["Mem_info"].create(self.engine)

def main():
	create_db_tables()
	db_conn()

if __name__ == '__main__':
	main()
