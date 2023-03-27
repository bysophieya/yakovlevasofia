bukva={1:"АВЕИНОРСТ",2:"ДКЛМПУ",3:"БГЁЬЯ",4:"ЙЫ",5:"ЖЗХЦЧ",8:"ШЭЮ",10:"ФЩЪ"}
slovo=input('Введите слово ').upper()
print('За это слово вы получаете', sum([k for i in slovo for k, v in bukva.items() if i in v]), 'очков')