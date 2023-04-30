class Restaurant:
    def __init__(self,restaurant_name,cuisine_type,rating):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.rating=rating
    def describe_restaurant(self):
        print('Название ресторана: ',self.restaurant_name, '\nКухня ресторана: ',self.cuisine_type,'\nРейтинг',self.rating)
    def open_restaurant(self):
        print('Ресторан открыт к посещению !')
    def change_rating(self,newrating):
        self.rating=newrating
newRestaurant=Restaurant('Марчеллис','Итальянская',4)
newRestaurant.describe_restaurant()
newRestaurant.change_rating(3)
newRestaurant.describe_restaurant()
