def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
   # return arr
my_list = []
print("Enter array :")
for i in range(5):
   hello =int( input())
   my_list.append(hello)
    
print(my_list)
bubble_sort(my_list)
print(my_list)

print(my_list[::-1])