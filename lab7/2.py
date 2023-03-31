from PIL import Image,ImageOps
image=Image.open(r'C:\Users\User\Desktop\cat.jpg')
image2= image.reduce(3)
image2 = ImageOps.mirror(image2)
image2 = ImageOps.flip(image2)
image.show()
image2.show()
image2.save(r'C:\Users\User\Desktop\newcat.jpg')