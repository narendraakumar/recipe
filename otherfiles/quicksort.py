


from operator import le


def quicksort(arr):

    pass

def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]
    return arr


def partition(arr,i,j):
    pivot = arr[j]
    pointer = i
    for k in range(i,j):
        if arr[k]<=pivot:
            arr = swap(arr,k,pointer)
            pointer+=1
    swap(arr,pointer,j)
    return pointer

def quicksort(l, r, nums):
    if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return nums
    if l < r:
        pi = partition(nums,l, r)
        quicksort(l, pi-1, nums)  # Recursively sorting the left values
        quicksort(pi+1, r, nums)  # Recursively sorting the right values
    return nums
 
if __name__ == '__main__':
    
    array = [4, 2, 3, 8, 8, 43, 6,1, 0]
    # partition(array,0,len(array)-1)
    quicksort(0,8,array)
    print(array)            