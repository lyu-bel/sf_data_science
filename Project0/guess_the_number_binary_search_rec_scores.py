# Вызов функции бинарного поиска с рекурсией
def binary_search_rec(number, count, low, high):
    mid = (low+high)//2
    count += 1  
    
    if mid == number:
      return count
    
    if mid < number:
      low = mid
      return binary_search_rec(number,count, low, high)  
    
    if mid > number:
      high = mid
      return binary_search_rec(number, count, low, high)


# Вызов функции нахождения среднего количества попыток угадывания числа за 1000 подходов
def score_game(binary_search_rec) -> int:
    n=100    # верхняя граница значений
    count=0  # счетчик кол-во попыток начальное значение
    low=0    # нижняя граница начальное значение
    high=n+1   # верхняя граница начальное значение
  
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(15) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(binary_search_rec(number,count, low, high))

    score = int(np.mean(count_ls)) # находим среднее количество попыток
    return(score)

# Вызов функции
import numpy as np

score_game=score_game(binary_search_rec)
print(f'Ваш алгоритм угадывает число в среднем за: {score_game} попыток')