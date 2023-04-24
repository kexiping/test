class Restaurant:
    """一个表示餐馆的类"""
    
    def __init__(self, name, cuisine_type):
        """初始化餐馆"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describer_restaurant(self):
        """显示餐馆信息摘要"""
        print(f"\n{self.name} serves wonderful {self.cuisine_type}")
        
    def open_restaurant(self):
        """指出餐馆正在营业"""
        print(f"{self.name} is open ,come in!")
    
    def set_number_served(self, number_served):
        """让用户能够设置就餐人数"""
        self.number_served = number_served
        
    def increment_number_served(self, additional_served):
        """让用户能够增加就餐人数"""
        self.number_served += additional_served
        
restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describer_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 430
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(1257)
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(239)
print(f"Number served: {restaurant.number_served}")

# print(restaurant.name)
# print(restaurant.cuisine_type)

# restaurant.describer_restaurant()
# restaurant.open_restaurant()   

# ludvigs = Restaurant("ludvigs's bistro", 'seafood')
# ludvigs.describer_restaurant()

# mango_thai = Restaurant('mango thai', ' thai food')   
# mango_thai.describer_restaurant()

