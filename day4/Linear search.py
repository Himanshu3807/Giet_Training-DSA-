#Linear Search in Python
#time complexity = BigOh(n)
def linearsearch(array,n,x):
    for i in range(0,n):
        if(array[i]==x):
            return i
    return -1
array = [2,4,0,1,9]
x = 9
n=len(array)
result = linearsearch(array,n,x)
if(result == -1):
    print("Element not Found")
else:
    print("Element found at index:",result)
