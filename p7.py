import random

import numpy as np
import pandas as pd


# Кількість симуляцій
num_simulations = 1000000

# Ініціалізація підрахунку сум
sum_counts = []
for i in range(11):
    sum_counts.append(0)

# Симуляція
for _ in range(num_simulations):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    sum_counts[total-2] += 1

# Обчислення ймовірностей
probabilities = []
for i in range(11):
    probabilities.append(sum_counts[i]/num_simulations)

# Теоретичні ймовірності
theoretical = [
     1/36,  2/36,  3/36,  4/36,  5/36,
     6/36, 5/36, 4/36, 3/36, 2/36, 1/36]

# Таблиця 
df = pd.DataFrame({
    "Сума": list(range(2,13)),
    "Ймовірність (Монте-Карло)": probabilities,
    "Ймовірність (Теоретична)": theoretical
})

# Відображення таблиці
print(df.to_string(index=False)
)
