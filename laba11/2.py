class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print('Название ресторана: ',self.restaurant_name, '\nКухня ресторана: ',self.cuisine_type)
    def open_restaurant(self):
        print('Ресторан открыт к посещению !')
newRestaurant=Restaurant('Марчеллис','Итальянская')
secondRestaurant=Restaurant('Сон','Японская')
thirdRestaurant=Restaurant('Friends','Грузинская')
newRestaurant.describe_restaurant()
secondRestaurant.describe_restaurant()
thirdRestaurant.describe_restaurant()