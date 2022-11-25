def binary_search():
    import numpy as np
    n = 100
    number = np.random.randint(1, n+1) # загадываем число
    count=0  #число попыток 
    low = 0  #наменьшее значение
    high = n+1 #наибольшее значение
    while low<=high:
        count+=1
        mid = (low+high)//2
        if mid<number:
            low=mid
        if mid>number:
            high=mid
        if mid==number:
            return count

# Function call 
sum=0
for i in range(1000):
    sum+=binary_search()
print(f'Программа угадает ваше число в среднем за {sum/1000} попыток')