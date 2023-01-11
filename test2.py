import random as r
def plusMinus(arr):
    count_min,count_zero,count_plus = 0,0,0 # Assign the initial values as 0
    for num in arr:
        if num == 0:
            count_zero += 1
        elif num > 0:
            count_plus += 1
        elif num < 0:
            count_min += 1
    print(format(count_plus/len(arr),'.6f'))
    print(format(count_min/len(arr),'.6f'))
    print(format(count_zero/len(arr),'.6f'))
    

n = int(input("Input n value: "))
arr = []
if n > 0 and n <= 100:
    for i in range(n):
        arr.append(r.randint(-100,100))
    print(arr)
    plusMinus(arr)
else:
    print("Invalid n value!")