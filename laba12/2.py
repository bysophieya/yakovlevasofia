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
        print("Сорты мороженого: ", self.flavors)
IceCreamStand=IceCreamStand('Шоколадное')
print(IceCreamStand.sorts())