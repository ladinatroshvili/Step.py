class Product:
    store_name = "TechShop Georgia" 
    currency = "GEL"
    total_products = 0 
    def __init__(self, name, price, stock, category, discount=0):
        self.name = name
        self.stock = stock
        self.price = price
        self.category = category
        self.discount = discount
        Product.total_products += 1
    def calculate_final_price(self):
        return self.price - (self.price * self.discount / 100)
    def get_info(self):
        return f"პროდუქტი: {self.name}, ფასი: {self.price}, რაოდენობა: {self.stock}, კატეგორია: {self.category}, ფასდაკლება: {self.discount}%"

    def apply_discount(self,percent):
        if percent < 0 or percent > 100:
            print("შეცდომა: ფასდაკლება უნდა იყოს 0%-დან 100%-მდე.")
        else:
            self.discount=percent
            print(f"ფასდაკლება არის  {self.discount}%")
    def update_stock(self, amount):
        new_stock = self.stock + amount
        if new_stock < 0:
            print("შეცდომა: მარაგი არ შეიძლება იყოს უარყოფითი.")
        else:
            self.stock = new_stock
            print(f"განახლებული მარაგი: {self.name} ----> {self.stock} ცალი")

    @classmethod
    def get_total_products_count(cls):
        return cls.total_products

p1=Product("Laptop", 1500, 10, "Electronics",50)
p2=Product("Mouse", 20, 50, "Electronics", 10)
p3=Product("Keyboard", 100, 30, "Electronics", 5)
p4=Product("Monitor", 300, 20, "Electronics", 15)
p5=Product("Cable", 10, 100, "Electronics", 0)

# print(p1.get_info())
# print(p2.get_info())
# print(p3.get_info())
# print(p4.get_info())
# print(p5.get_info())
# print(f"საბოლოო ფასი {p1.name}: {p1.calculate_final_price()} {Product.currency}")
# print(f"საბოლოო ფასი {p2.name}: {p2.calculate_final_price()} {Product.currency}")
# print(f"საბოლოო ფასი {p3.name}: {p3.calculate_final_price()} {Product.currency}")
# print(f"საბოლოო ფასი {p4.name}: {p4.calculate_final_price()} {Product.currency}")
# print(f"საბოლოო ფასი {p5.name}: {p5.calculate_final_price()} {Product.currency}")
# print(Product.get_total_products_count())
# print(p5.get_info())
# p5.apply_discount(15)
# print(f"საბოლოო ფასი ფასდაკლებით: {p5.calculate_final_price()} {Product.currency}")
# p3.update_stock(5)  
# p3.update_stock(-5) 
# p1.update_stock(10)  
# p2.update_stock(-5) 
# p4.update_stock(5)   
p1.apply_discount(20)  
# p1.apply_discount(1)
# print(p1.get_info())
# print(p1.calculate_final_price())