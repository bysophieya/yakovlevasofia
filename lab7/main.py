from PIL import Image
image=Image.open('C:/Users/User/Desktop/cat.jpg')
image.show()
print(image.size)
print(image.format)
print(image.mode)