"""
Основные Routers проекта, вынесенные в отдельный файл

"""

import json
import os
import random
from pathlib import Path
from fastapi import APIRouter, Depends, UploadFile, File, Body
from fastapi.requests import Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, delete
from appW import templates
from appW.bd import get_session, Declar_Memes
from appW.bd.db_MinIO import InpFile, DelFile
from appW.bd.schemas import Rat_files, WorkerInd, Rat_upp


router = APIRouter(
	prefix='/Operatro',
	tags=['operation']
)
@router.get('/memes')
async def get_all_memes(request: Request, session: AsyncSession = Depends(get_session)):
	"""
	Доменная страница проекта
	Получить список мемов
	"""
	items = (select(Declar_Memes))
	all_items = await session.execute(items)
	itemir = all_items.scalars().all()
	await session.commit()
	result = [WorkerInd.model_validate(row, from_attributes=True) for row in itemir]

	list = {}
	ll = {}
	for ii, el in zip(range(len(result)), result):
		for i in el:
			ll[str(i[0])] = i[1]
		ll2 = json.dumps(ll)
		lll = json.loads(ll2)
		list[str(ii)] = lll
	i1 = json.dumps(list)
	i2 = json.loads(i1)

	return templates.TemplateResponse(name='all_memes.html', context={'request': request, 'db_data': i2})

@router.get('/memes/{id_}')
async def get_id_memes(id_: str, request: Request, session: AsyncSession = Depends(get_session)):
	"""
	Открывает страницу с отдельным мемом в полном развороте
	Получить конкретный мем
	"""
	qwert = select(Declar_Memes).where(Declar_Memes.id == int(id_))
	item = await session.execute(qwert)
	result = item.scalars()
	await session.commit()
	for el in result:
		search = {1: el.id, 2:el.name, 3:el.des_, 4:el.Img_id}
	return templates.TemplateResponse(name='init_meme.html',
									  context={
										  'request': request,
										  'id': search[1],
										  'name': search[2],
										  'descr': search[3],
										  'imgas': search[4]
										  })

@router.post('/memes')
async def new_mem(users_rev: Rat_files = Body(...), image: UploadFile = File(...), session: AsyncSession = Depends(get_session)):
	"""Добавить новый мем"""
	img_data = await image.read()
	ID_image = await name_fileD(users_rev.name)

	query = insert(Declar_Memes).values(
		[{
			'name': users_rev.name,
			'des_': users_rev.descr,
			'Img_id': ID_image
		}])
	itemsQuery = await session.execute(query)
	itemsCommit = await session.commit()

	SAVES = Path() / 'appW/images_static'
	save_to = SAVES / ID_image
	files_img = open(save_to, 'wb')
	files_img.write(img_data)
	files_img.close()

	pather = os.path.abspath(save_to)

	await InpFile(ID_image, pather)
	os.remove(pather)
	return {'filename Saved!': image.filename}

@router.put('/memes/{id}')
async def update_mem(id:str,
					 users_rev: Rat_upp = Body(...),
					 image: UploadFile = File(...),
					 session: AsyncSession = Depends(get_session)):
	"""Обновить существующий мем"""
	img_data = await image.read()
	imgNAME = users_rev.imgDel.split('/')[-1]

	tbl = {
			'name': users_rev.name,
			'des_': users_rev.descr,
		}
	quert = update(Declar_Memes).where(Declar_Memes.id == int(id)).values(name=users_rev.name, des_=users_rev.descr)
	comm = await session.execute(quert)
	await session.commit()


	SAVES = Path() / 'appW/images_static'
	save_to = SAVES / imgNAME
	files_img = open(save_to, 'wb')
	files_img.write(img_data)
	files_img.close()
	pather = os.path.abspath(save_to)
	await InpFile(imgNAME, pather)
	return {'Update': 'Accept!'}

@router.delete('/memes/{id}')
async def delete_mem(id:str, session: AsyncSession = Depends(get_session)):
	"""Удалить мем"""

	querter = select(Declar_Memes).where(Declar_Memes.id == int(id))
	items = await session.execute(querter)
	await session.commit()

	imgdel = Path() / 'appW/images_static'
	for el in items.scalars():
		chs = el.Img_id
	os.remove(f'{imgdel}/{chs}')

	query = delete(Declar_Memes).where(Declar_Memes.id == int(id))
	await session.execute(query)
	await session.commit()
	await DelFile(chs)


	return {'Delete': 'comlete'}

async def name_fileD(Named):
	"""Генератор случайной метки изображений"""
	idimg = str(random.randint(1, 1000000))+"_"+str(Named[0:100])+'.jpg'
	return idimg