tickets=int(input("Введите количество билетов:"))
ages =[]
value = 1
cost_sum = 0


while value < tickets + 1:
    age_value = int(input("Введите полный возраст посетителя для билета № %s: " % value))
    ages.append(age_value)
    value += 1

for age in ages:
    if age < 18:
        cost = 0
    elif age >= 25:
        cost = 1390  
    else:
        cost = 990
        
    cost_sum += cost    
    

if tickets >= 3:
    cost_sum -= cost_sum*0.1
    print("Сумма к оплате со скидкой при покупке более трех билетов: %s" % cost_sum)
else:
    print("Сумма к оплате: %s" % cost_sum)