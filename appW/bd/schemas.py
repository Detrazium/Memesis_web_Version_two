"""
Pydantic схемы для проверки и валидации данных
"""


import json
from pydantic import BaseModel, model_validator
from sqlalchemy import Integer, String, Text, Column, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Table_MODEL(Base):
	"""Основная модель таблицы"""
	__tablename__ = 'Mem_info'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String, nullable=False)
	des_ = Column(Text, nullable=False)
	Img_id = Column(Text)

class WorkerUpp(BaseModel):
	id: int
class WorkerInd(WorkerUpp):
	name: str
	des_: str
	Img_id: str


met = MetaData()
Memes_model = Table(
	'Mem_info', met,
Column('id', Integer, autoincrement=True, primary_key=True),
	 Column('name', String, nullable=False),
	 Column('des_', Text, nullable=False),
	 Column('Img_id', Text)
					)
class Rat_files(BaseModel):
	name: str
	descr: str
	@model_validator(mode='before')
	@classmethod
	def validate_to_json(cls, value):
		if isinstance(value, str):
			return cls(**json.loads(value))
		return value
class Rat_upp(BaseModel):
	name: str
	descr: str
	imgDel: str
	@model_validator(mode='before')
	@classmethod
	def validate_to_json(cls, value):
		if isinstance(value, str):
			return cls(**json.loads(value))
		return value
