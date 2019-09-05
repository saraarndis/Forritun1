num1 = 0
num2 = 0
list1 = []
for num1 in range(1 , 100 + 1):
    for i in range (1 , 100 + 1):
        if (num1 % i == 0):
            list1.append(num1)
            print(list1.count(48))
    