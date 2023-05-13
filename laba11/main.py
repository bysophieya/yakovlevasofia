class Restaurant: 
    def __init__(self,restaurant_name,cuisine_type): #содержит 2 атрибута
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print('Название ресторана: ',self.restaurant_name, '\nКухня ресторана: ',self.cuisine_type)
    def open_restaurant(self):
        print('Ресторан открыт к посещению !')
newRestaurant=Restaurant('Марчеллис','Итальянская') #экземпляр со своими входными данными
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
