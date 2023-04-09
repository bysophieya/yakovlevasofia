from PIL import Image,ImageOps
image=Image.open('C:/Users/User/Desktop/cat.jpg')
image2= image.reduce(3) #Метод возвращает копию изображения, уменьшенную в 3 раза.
image2 = ImageOps.mirror(image2) #зеркально отражает по горизонтали (слева направо).
image2 = ImageOps.flip(image2) #переворачивает вертикально (сверху вниз).
image.show()
image2.show()
image2.save('C:/Users/User/Desktop/newcat.jpg')