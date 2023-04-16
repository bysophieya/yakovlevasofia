from PIL import Image
import numpy as np

img = Image.open('picture.jpg')
img_arr = np.array(img) #Изображения преобразуются в массив Numpy в формате высоты, ширины, канала.

img_arr[0: 400, 0: 200] = (0, 0, 0) #мы удалили бы пиксели в области от (0,0) до (400, 200) (верхняя левая сторона)
img = Image.fromarray(img_arr)
img.show()
img.save('newpicture.jpg')