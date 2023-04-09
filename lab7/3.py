from PIL import Image,ImageFilter
images=['первый.jpg','второй.jpg','третий.jpg','четвертый.jpg','пятый.jpg']
for img in images: #создаем цикл и пробегаемся по каждой фотке
    image= Image.open(img)
    img_f= image.filter(ImageFilter.FIND_EDGES) #накладываем фильтр выделения краев
    img_f.save('filters/'+str(img)) #сохраняем с новым названием с помощью переменной img