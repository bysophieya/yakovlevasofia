class Restaurant:
    def __init__(self,restaurant_name,cuisine_type): #содержит 2 атрибута
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print('Название ресторана: ',self.restaurant_name, '\nКухня ресторана: ',self.cuisine_type)
    def open_restaurant(self):
        print('Ресторан открыт к посещению !')
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_menu(self):
        for flavor in self.flavors:
            print(flavor)
IceCreamStand1=IceCreamStand('Марчеллис','Итальянская',['Шоколадное',"Клубничное"])
print(IceCreamStand1.sorts())