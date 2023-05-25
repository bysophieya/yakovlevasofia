import json #формат передачи данных, который используется при взаимодействии веб-сервера и браузера

def print_product_info(product):
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии")
    print() # выводим пустую строку для разделения продуктов
with open("products.json", "r", encoding='utf-8') as f:
    products2 = json.load(f) # загружаем данные из файла в переменную,десериализация

products = products2["products"] # получаем список продуктов из словаря products2

list(map(print_product_info, products)) # применяем функцию print_product_info ко всем элементам списка products с помощью функции map
