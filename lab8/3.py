from PIL import Image,ImageDraw,ImageFont
img = Image.open('picture.jpg')
img_crop=img.crop((0,30,564,591))
img_crop.save('newpicture.jpg')
name=input('Кого вы хотите поздравить? ')
draw_text = ImageDraw.Draw(img) #изображения для рисования
myFont = ImageFont.truetype('Montserrat-Regular.ttf', 40) # подключаем шрифт
draw_text.text(
    (90,50), #расположение
    '{},поздравляю!'.format(name), #форматирование строк
    font=myFont,
    stroke_width=2, #Ширина обводки текста.
    fill=(255, 255, 255),
    )
img.show()
img.save('newpicture.png')