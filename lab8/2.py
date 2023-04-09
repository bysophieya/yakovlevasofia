holidays={"8 марта":'8марта.jpg',"14 февраля":'14февраля.jpg',"День рождения":'др.jpg',"Рождество":'рождество.jpg'}
prazdnik=input('К какому празднику вы хотите открытку?')
filename = holidays[prazdnik]
with open(filename, 'rb') as f:
    image = f.read()
filename = image
