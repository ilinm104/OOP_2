def read_cookbook(file_path):
    cook_book = {}

    with open(file_path, encoding="utf-8") as file:
        while True:
            # Чтение названия рецепта
            dish_name = file.readline().strip()

            if not dish_name:
                break  # Если достигли конца файла, выходим из цикла

            # Чтение количества ингредиентов
            ingredient_count = int(file.readline().strip())

            # Чтение списка ингредиентов
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_line = (
                    file.readline().strip()
                )  # Чтение строки с ингредиентом
                ingredient_data = ingredient_line.split(
                    " | "
                )  # Разделение строки на части
                ingredient_dict = {
                    "ingredient_name": ingredient_data[0],
                    "quantity": int(ingredient_data[1]),
                    "measure": ingredient_data[2],
                }
                ingredients.append(ingredient_dict)

            # Добавляем блюдо в словарь
            cook_book[dish_name] = ingredients

            # Пропускаем пустую строку между рецептами
            file.readline()

    return cook_book


# Пример использования функции
file_path = "C:\\Python\\cookbook.txt"  # Путь к вашему файлу с рецептами
cookbook = read_cookbook(file_path)
print(cookbook)
