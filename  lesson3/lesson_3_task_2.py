from smartphone import Smartphone

# Создаем пустой список для каталога
catalog = []

# Наполняем список пятью разными экземплярами класса Smartphone
catalog.append(Smartphone("Apple", "iPhone 15", "+79111282536"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79219873625"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+79035558521"))
catalog.append(Smartphone("Google", "Pixel 8", "+79066669512"))
catalog.append(Smartphone("OnePlus", "12", "+79551117458"))

# Цикл для печати всего каталога
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")