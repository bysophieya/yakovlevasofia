import os
from PIL import Image,ImageFilter

os.makedirs("itog", exist_ok=True) #создает все промежуточные каталоги

for filename in os.listdir("photos"): # перебор файлов в каталоге,возвращает список, содержащий имена файлов
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        with Image.open(os.path.join("photos", filename)) as img: #правильно соединяет переданный путь path к одному или более компонентов пути
            img= img.filter(ImageFilter.FIND_EDGES)
            img2 = os.path.join("itog", filename)
            img.save(img2)