"""
Функция удаления фотографий из временной папки при отключении проекта
"""
import os
import shutil
def Del_ImgStart():
    folder = 'appW/images_static'
    for files in os.listdir(folder):
        file_pattt = os.path.join(folder, files)
        try:
            if os.path.isfile(file_pattt) or os.path.islink(file_pattt):
                os.unlink(file_pattt)
            elif os.path.isdir(file_pattt):
                shutil.rmtree(file_pattt)
        except Exception as e:
            print('failed_del')

def main():
    Del_ImgStart()

if __name__ == '__main__':
    main()