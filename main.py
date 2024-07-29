import uvicorn
"""Локальный запуск из проекта напрямую"""
if __name__ =='__main__':
	uvicorn.run('appW.core:app', host='localhost', port=8010, reload=True)