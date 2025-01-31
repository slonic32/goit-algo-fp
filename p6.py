class Dish:
    def __init__(self, name, price, calorie):
        self.name = name
        self.price = price
        self.calorie = calorie
        self.ratio = calorie / price

def greedy_algorithm(menu: list[Dish], budget: int):
    menu.sort(key=lambda x: x.ratio, reverse=True)
    dishes = []
    total_price = 0
    total_value = 0
    for dish in menu:
        if budget >= dish.price:
            budget -= dish.price
            total_price += dish.price
            total_value += dish.calorie
            dishes.append(dish.name)
    return dishes, total_price, total_value

def dynamic_programming(menu: list[Dish], budget: int):
    dishes = []
    total_price = 0
    total_value = 0
    n = len(menu)
    # створюємо таблицю K для зберігання оптимальних значень підзадач
    K = [[0 for w in range(budget + 1)] for i in range(n + 1)]

    # будуємо таблицю K знизу вгору
    for i in range(n + 1):
        for w in range(budget + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif menu[i - 1].price <= w:
                K[i][w] = max(menu[i - 1].calorie + K[i - 1][w - menu[i - 1].price], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # Відновлення вибраних страв
    total_value = K[n][budget]
    w = budget
    chosen_dishes = []
    for i in range(n, 0, -1):
        if K[i][w] != K[i - 1][w]:  # Якщо  страва була взята
            chosen_dishes.append(menu[i - 1].name)
            w -= menu[i - 1].price

    total_price = budget - w
    return chosen_dishes, total_price, total_value




# Меню
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

menu = []

for item, details in items.items():
    menu.append(Dish(item, details['cost'], details['calories']))

# Бюджет
budget = 100

# Виклик функції
print("Жадібний алгоритм: ", greedy_algorithm(menu, budget))  

print("Динамічний алгоритм: ", dynamic_programming(menu, budget))
