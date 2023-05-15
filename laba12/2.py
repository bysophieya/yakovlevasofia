class Restaurant:
    def __init__(self,restaurant_name,cuisine_type): #содержит 2 атрибута
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print('Название ресторана: ',self.restaurant_name, '\nКухня ресторана: ',self.cuisine_type)
    def open_restaurant(self):
        print('Ресторан открыт к посещению !')
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors,location,time):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors=flavors
        self.location = location
        self.time = time

    def sorts(self):
        for flavor in self.flavors:
            print(flavor)
    def change_flavors(self,newflavors):
        self.flavors=newflavors
    def check_flavors(self):
        if sort in self.flavors:
            print("Есть в наличие")
        else:
            print("Такого сорта нет")
IceCreamStand1=IceCreamStand('Марчеллис','Итальянская',['Шоколадное',"Клубничное"],'Петроградская','12:00-18:00')
print(IceCreamStand1.sorts())
IceCreamStand1.change_flavors(['Клубничное','Шоколадное',"Ванильное"])
print(IceCreamStand1.sorts())
sort=input("Введите сорт мороженого ")
print(IceCreamStand1.check_flavors())