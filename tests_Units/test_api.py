"""

Пара простых на проверку базы данных и сервера
имеют смысл только при запущенной базе данных

"""
import unittest
import uvicorn
from appW.bd import create_db_tables
from appW.bd.db_MinIO import client


class fastapi_tests_routers(unittest.TestCase):
    def test_fastappi_core(self):
        uvicorn.run('appW.core:app', host='0.0.0.0', port=8000, reload=True)
    def test_db(self):
        create_db_tables()


