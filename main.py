def read_cook_book(file_path):
    """
  Читает файл с рецептами и создает словарь cook_book.
  """
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredients_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredients_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
            file.readline()  # Пропуск пустой строки между рецептами
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    """
  Формирует список покупок для заданных блюд и количества персон.
  """
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            print(f"Блюдо '{dish}' отсутствует в книге рецептов")
            continue
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {
                    'measure': ingredient['measure'],
                    'quantity': quantity
                }
    return shop_list


# Пример использования
if __name__ == "__main__":
    # Задача №1: Чтение файла и создание словаря cook_book
    file_path = 'cook_book.txt'
    try:
        cook_book = read_cook_book(file_path)
        print("Книга рецептов успешно прочитана:")
        for dish, ingredients in cook_book.items():
            print(f"{dish}: {ingredients}")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден. Проверьте путь к файлу.")
        exit()

    # Задача №2: Получение списка покупок
    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2
    shopping_list = get_shop_list_by_dishes(dishes, person_count, cook_book)

    print("\nСписок покупок:")
    for ingredient, details in shopping_list.items():
        print(f"{ingredient}: {details}")