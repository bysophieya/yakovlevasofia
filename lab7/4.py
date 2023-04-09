from PIL import Image,ImageDraw,ImageFont
img=Image.open('котик.jpg')
z=Image.open('знак.png')
img.paste(z,(0,0), mask=z) #Метод paste всталяет одно изображение в другое изображение  с координатами в угол,знак используется как маска
img.show()