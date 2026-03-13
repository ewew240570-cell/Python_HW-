from smartphone import Smartphone


catalog = []


catalog.append(Smartphone("Apple", "iPhone 15 Pro", "+791..."))
catalog.append(Smartphone("Samsung", "Galaxy S20 Ultra", "+792..."))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+793..."))
catalog.append(Smartphone("Google", "Pixel 8 Pro", "+794..."))
catalog.append(Smartphone("OnePlus", "12", "+795..."))

# Печатаем весь каталог в нужном формате
print("Каталог смартфонов:")
print("-" * 30)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
