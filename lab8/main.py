from PIL import Image
import numpy as np

img = Image.open('picture.jpg')
img_arr = np.array(img) #Изображения преобразуются в массив Numpy в формате высоты, ширины, канала.

img_arr[0: 400, 0: 200] = (0, 0, 0) #мы удалили бы пиксели в области от (0,0) до (400, 200) (верхняя левая сторона)
img = Image.fromarray(img_arr)
img.show()
img.save('newpicture.jpg')

from PIL import Image

name = "plita.jpg"
with Image.open(name) as img:
    img.load()


width, heigth = img.size
print(img.size)

img = img.crop((270, 120, 400, 310))
img2 = img.save("ddd.jpg")
img.crop=img.show()
