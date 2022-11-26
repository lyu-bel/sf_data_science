def binary_search_rec(number, count, low, high): #Бинарный поиск с рекурсией с циклом 1000 прохождений
    mid = (low+high)//2
    count+=1  #число попыток 
    if mid==number:
      return count
    if mid<number:
      low=mid
      return binary_search_rec(number,count, low, high)  
    if mid>number:
      high=mid
      return binary_search_rec(number, count, low,high)


# Function call
import numpy as np
n=100
sum=0

for i in range (1000):
  number = np.random.randint(1, n+1) # загадываем число
  count=0
  low = 0  #наменьшее значение
  high = n+1 #наибольшее значение
  sum+=binary_search_rec(number, count, low,high)

print(f'Программа угадает ваше число в среднем за {sum/1000} попыток')