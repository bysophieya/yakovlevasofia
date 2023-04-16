from PIL import Image,ImageDraw,ImageFont
img = Image.open('picture.jpg')
img_crop=img.crop((0, 30, 564, 591))
img_crop.save('newpicture.jpg')
name=input('Кого вы хотите поздравить? ')
draw_text = ImageDraw.Draw(img) #изображения для рисования
myFont = ImageFont.truetype('Montserrat-Regular.ttf', 40) # подключаем шрифт
draw_text.text(
    (90,50), #расположение
    '{},поздравляю!'.format(name), #форматирует строки
    font=myFont,
    stroke_width=2, #ширина обводки текста
    fill=(0, 0, 0),
    )
img.show()
img.save('newpicture.png')