def BubbleSort(array): #Сортировка введенных чисел
	for i in range(len(array)):
		for j in range(len(array)-i-1):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
	return array
 


def BinarySearchUpgr(array, element, left, right):  #Поиск который меньше введенного числа, а следующий за ним больше или равен этому числу
    if left > right: 
        return right  
    
    middle = (right+left) // 2  
    if array[middle] == element:  
        i = middle
        while array[i] == array[i-1]:
            i -= 1
        return i - 1
    elif element < array[middle]: 
        return BinarySearchUpgr(array, element, left, middle-1)
    else: 
        return BinarySearchUpgr(array, element, middle+1, right)
				
num_list = []
value = 0

while True:  
    try:
        num_list = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
        if len(num_list) == 0:
            print("Некорректный ввод")
            continue
        break
    except ValueError:
        print("Некорректный ввод")

 
	
while True:
    try:
        value = int(input("Введите любое число: "))
        
    except ValueError:
        print("Некорректный ввод")
        continue
         
    if value > max(num_list):
        print("Введенное число превышает максимальное значение элемента введенной последовательности")
    elif value <= min(num_list):
        print("Введенное число меньше минимального значения элемента введенной последовательности")
    else:
        break               
            

sort_num_list = BubbleSort(num_list)                      
result = BinarySearchUpgr(sort_num_list, value, 0, len(num_list)-1)

print("Отсортированная последовательность: ", sort_num_list)
print("Номер позиции элемента, который меньше введенного числа, а следующий за ним больше или равен этому числу: ", result)