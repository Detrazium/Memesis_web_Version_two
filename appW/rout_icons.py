"""

Роутеры отображения фотографий и иконок действий

"""

from fastapi import APIRouter, Response
from fastapi.responses import FileResponse
from appW.bd.db_MinIO import GetFile

router = APIRouter(
	prefix='/icons',
	tags=['icon']
)
@router.get('/update.ico', include_in_schema=False)
async def favicon():
	"""
	Иконка обновления
	"""
	return FileResponse('appW/icon/update.ico')
@router.get('/select.ico', include_in_schema=False)
async def favicon2():
	"""
	Иконка выбора
	"""
	return FileResponse('appW/icon/select.ico')
@router.get('/delete.ico', include_in_schema=False)
async def favicon3():
	"""
	Иконка удаления
	"""
	return FileResponse('appW/icon/delete.ico')
@router.get('/return.ico', include_in_schema=False)
async def favicon4():
	"""
	Иконка возврата
	"""
	return FileResponse('appW/icon/return_ico.ico')



rute_img = APIRouter(
	prefix='/imGG',
	tags=['image']
)
@rute_img.get('/{img}', include_in_schema=False)
async def imager_get(img: str):
	"""Отдельный роутер для вывода фотографий"""
	await GetFile(img)
	old = f'appW/images_static/{img}'
	return FileResponse(old)