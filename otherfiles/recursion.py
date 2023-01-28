def fac(n):
    if n == 1:
        return 1

    else:
        return n*fac(n-1)

def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)

def nthtermofgp(n,m):
    if n == 1:
        return m
    else:
        return m*nthtermofgp(n-1,m)

def tower_of_hanoi(disks, source, auxiliary, target):  
    if(disks == 1):  
        print('Move disk 1 from rod {} to rod {}.'.format(source, target))  
        return  
    # function call itself  
    tower_of_hanoi(disks - 1, source, target, auxiliary)  
    print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))  
    tower_of_hanoi(disks - 1, auxiliary, source, target)

def merge_sort(array):
    ret = []
    if( len(array) == 1):
        return array;
    half  = len(array) / 2
    lower = merge_sort(array[:half])
    upper = merge_sort(array[half:])
    lower_len = len(lower)
    upper_len = len(upper)
    i = 0
    j = 0
    while i != lower_len or j != upper_len:
        if( i != lower_len and (j == upper_len or lower[i] < upper[j])):
            ret.append(lower[i])
            i += 1
        else:
            ret.append(upper[j])
            j += 1

    return ret




if __name__ == '__main__':
    array = [4, 2, 3, 8, 8, 43, 6,1, 0]
    ar = merge_sort(array)
    print( " ".join(str(x) for x in ar)   )   