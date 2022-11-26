def binary_search():
    import numpy as np
    n = 100
    number = np.random.randint(1, n+1) # загадываем число
    count = 0                          
    low = 0                            
    high = n+1                         
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
sum_runs = 0
for i in range(1000):
    sum_runs += binary_search()
print(f'Программа угадает ваше число в среднем за {sum_runs/1000} попыток')