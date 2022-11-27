def binary_search(number,count, low, high): #Бинарный поиск с циклом 1000 прохождений
    
    while low <= high:
        count += 1
        mid = (low+high) //2
        
        if mid < number:
            low = mid
            
        if mid > number:
            high = mid
            
        if mid == number:
            return count


# Вызов функции нахождения количества попыток в среднем из 1000 подходов угадывает наш алгоритм
def score_game(binary_search) -> int:
    n=100    # верхняя граница значений
    count=0  # счетчик кол-во попыток начальное значение
    low=0    # нижняя граница начальное значение
    high=n+1   # верхняя граница начальное значение
  
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(binary_search(number,count, low, high))

    score = int(np.mean(count_ls)) # находим среднее количество попыток
    return(score)

# Вызов функции
import numpy as np

score_game=score_game(binary_search)
print(f'Ваш алгоритм угадывает число в среднем за: {score_game} попыток')