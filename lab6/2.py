bukva={1:"АВЕИНОРСТ",2:"ДКЛМПУ",3:"БГЁЬЯ",4:"ЙЫ",5:"ЖЗХЦЧ",8:"ШЭЮ",10:"ФЩЪ"}
slovo=input('Введите слово ').upper() #делаем буквы в большом регистре
print('За это слово вы получаете', sum([k for i in slovo for k, v in bukva.items() if i in v]), 'очков')
# for i in slovo - перебираем каждый символ в строке slovo
# for k, v in bukva.items()- перебираем каждую пару ключ-значение (k- ключ, v-значение)
# if i in v - есть ли символ в значении v текущей пары ключ-значение
