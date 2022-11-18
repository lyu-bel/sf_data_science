#guess the number
import numpy as np
n = 100
number = np.random.randint(1, n+1) # загадываем число
#number = 100
count=1
predict_number=n/2
if number>50:
    start_range=50
    end_range=101
if number<50:
    start_range=0
    end_range=50
while True:
    if predict_number==number:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break  
    while predict_number<number:
        prom_range=predict_number
        predict_number=(start_range+end_range)//2
        start_range=predict_number
        count +=1
        if predict_number>number:
            start_range=prom_range
            end_range=predict_number
            break
    while predict_number>number:
        prom_range=predict_number
        predict_number=(start_range+end_range)//2
        end_range=predict_number
        count +=1
        if predict_number<number:
            start_range=predict_number
            end_range=prom_range
            break