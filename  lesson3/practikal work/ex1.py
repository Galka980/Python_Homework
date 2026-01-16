from product import Product

my_product = Product("Laptop", 1200)

print(my_product.get_name())# Ожидаемый результат: "Laptop"
print(my_product.get_price())# Ожидаемый результат: 1200
print(my_product.get_product_info())# Ожидаемый результат: "Product: Laptop, Price: 1200"