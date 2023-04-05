def partition(array,low,high): # [8,7,6,1,0,9,2]
    pivot = array[high] # 2
    i = low-1 # i=-1
    for j in range(low,high): # 0 to 5
        if array[j]<=pivot:
            i = i+1
            (array[i],array[j])=(array[j],array[i])
    # swap the pivot element with the graeter element specified between
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1
# function to perform quicksort
def quicksort(array,low,high): # low=0 high=6
    if low<high:
        # find pivot element such that element smaller than pivot are on the left and element greater than pivot are on the right
        pi = partition(array,low,high)
        # recursive call on the left of the pivot
        quicksort(array,low,pi-1)
        # recursive call on the left of the pivot
        quicksort(array,pi+1,high)
data=[8,7,6,1,0,9,2]
print("Unsorted Array")
print(data)
size = len(data)
quicksort(data,0,size-1)
print("Sorted Array in asscending order:")
print(data)

