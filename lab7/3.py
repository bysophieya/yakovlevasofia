from PIL import Image,ImageFilter
images=['первый.jpg','второй.jpg','третий.jpg','четвертый.jpg','пятый.jpg']
for img in images: #создаем цикл и пробегаемся по каждой фотке
    with Image.open(img) as images:
        image= Image.open(img)
        img_f= image.filter(ImageFilter.FIND_EDGES) #накладываем фильтр выделения краев
        img_f.show()
        img_f.save('new'+img) #сохраняем с новым названием