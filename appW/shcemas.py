"""
Базовая схема проверки валдации приходящих json
"""
from pydantic import BaseModel

class baser(BaseModel):
	id: int
	name: str
	currenter: str
	DATOID: str
	base_id: int