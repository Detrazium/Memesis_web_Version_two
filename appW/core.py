"""

Корневой файл проекта объединяющий все роутеры

"""
import atexit
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from appW.bd.cleaner_image import Del_ImgStart
from appW.routers import router as router_operator
from appW.rout_icons import router as icon_rout, rute_img


def exit_handler():
	"""Локальная чистка подгруженных для отображения фотографий"""
	print('чистка подгруженных фотографий... ')
	Del_ImgStart()
atexit.register(exit_handler)


app = FastAPI(title='PAGE_NAEM_FRONT')
app.mount('/appW/static', StaticFiles(directory='appW/static'), name='static')
app.mount('/appW/images_static', StaticFiles(directory='appW/images_static'), name='images_static')
app.mount('/app/icon', StaticFiles(directory='appW/icon'), name='icon')
app.include_router(icon_rout)
app.include_router(router_operator)
app.include_router(rute_img)

