"""Подзагрузка fronted-a к fastapi"""
from starlette.templating import Jinja2Templates
templates = Jinja2Templates(directory='appW/templates')