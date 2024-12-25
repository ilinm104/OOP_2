def read_cookbook(file_path):

    cook_book = {}
    with open(file_path, encoding="utf-8") as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break

            ingredient_count = int(f.readline())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_info = f.readline().strip().split(" | ")
                name, quantity, measure = ingredient_info
                ingredients.append(
                    {
                        "ingredient_name": name,
                        "quantity": int(quantity),
                        "measure": measure,
                    }
                )

            cook_book[dish_name] = ingredients
            # Пустая строка между рецептами
            f.readline()
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):

    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book.get(dish, []):
            ingredient_name = ingredient["ingredient_name"]
            if ingredient_name in shop_list:
                shop_list[ingredient_name]["quantity"] += (
                    ingredient["quantity"] * person_count
                )
            else:
                shop_list[ingredient_name] = {
                    "measure": ingredient["measure"],
                    "quantity": ingredient["quantity"] * person_count,
                }
    return shop_list


# Чтение файла рецептов
cookbook_file = r"C:\Python\recipes.txt"
cook_book = read_cookbook(cookbook_file)

# Пример использования функции
result = get_shop_list_by_dishes(cook_book, ["Запеченный картофель", "Омлет"], 2)
print(result)
