from PIL import Image,ImageDraw,ImageFont
import numpy as np


img = Image.open('picture.jpg')
img_arr = np.array(img) #Изображения преобразуются в массив Numpy в формате высоты, ширины, канала.

img_arr[0: 400, 0: 200] = (0, 0, 0) #мы удалили бы пиксели в области от (0,0) до (400, 200) (верхняя левая сторона)
img = Image.fromarray(img_arr) #создает изображение в памяти из объекта obj
name=input('Кого вы хотите поздравить? ')
w=564
h=619
draw_text = ImageDraw.Draw(img) #изображения для рисования
myFont = ImageFont.truetype('Montserrat-Regular.ttf', 40) # подключаем шрифт
draw_text.text(
    (50,50), #расположение
    '{},поздравляю!'.format(name), #Подстановку данных можно сделать с помощью форматирования строк. 
    font=myFont,
    stroke_width=2, #yказывает ширину контура текущего объекта.
    fill=(0, 0, 255),
    )
img.show()
img.save('newpicture.png')
