from PIL import Image
img = Image.open('picture.jpg')
img_crop=img.crop((0,30,564,591))
img_crop.show()
img_crop.save('newpicture.jpg')