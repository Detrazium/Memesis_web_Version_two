"""Покдлючение функционала Minio"""

from miniopy_async import Minio as Async_minio


bucket = "python-bucket"
client = Async_minio(
    endpoint="localhost:9000",
    access_key="Detraz",
    secret_key="ASDFGHASDFGH",
    secure=False
)

async def InpFile(file_name, file_path):
    """Добавить файл в корзину minio"""
    try:
        await client.fput_object(
            bucket, file_name,file_path
        )
        print(
            'Minio успешно загрузил фото:', file_name, 'В корзину', bucket
        )
        await GetFile(file_name)
    except:
        print('Load File to minio ERROR')

async def GetFile(file_name):
    """Загрузить файл"""
    print('img_put')
    url = await client.fget_object(bucket_name=bucket, object_name=file_name, file_path='appW/images_static/'+file_name)
    return url

async def DelFile(file_name):
    """Удалить файл"""
    await client.remove_object(bucket_name=bucket, object_name=file_name)








