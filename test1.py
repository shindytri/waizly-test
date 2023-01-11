def miniMaxSum(arr):
    min,max = arr[0],arr[0] # Assign the initial value as the first number in array
    for num in arr:
        if num < min:
            min = num
        elif num > max:
            max = num
    min_sum = sum(arr) - max
    max_sum = sum(arr) - min
    print(min_sum,max_sum)
    
arr = [1,3,5,7,9]
print(arr)
miniMaxSum(arr)