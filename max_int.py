num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = 0 
list1 = []
while(num_int >= 0):
    list1.append(num_int)
    num_int = int(input("Input a number: "))
if(num_int < 0):
    max_int = max(list1)
print("The maximum is", max_int)    # Do not change this line