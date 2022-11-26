def binary_search_rec(number, count, low, high): #Бинарный поиск с рекурсией с циклом 1000 прохождений
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


# Вызов функции
import numpy as np
n = 100  #верхняя граница диапазона угадывания
sum = 0 

for i in range (1000):
  number = np.random.randint(1, n+1) # загадываем число
  count = 0   #счетчик попыток угадывания
  low = 0  #нижняя граница
  high = n+1 #верхняя граница
  sum += binary_search_rec(number, count, low, high)

print(f'Программа угадает ваше число в среднем за {sum/1000} попыток')