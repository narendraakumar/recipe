


def merge_sort(arr):

    if len(arr)>1:

        mid = len(arr)//2

        l1 = arr[:mid]
        l2 = arr[mid:]


        merge_sort(l1)
        merge_sort(l2)

        i,j = 0,0
        k = 0
        while i<len(l1) or j<len(l2):
            if len(l1)==i:
                for l,v in enumerate(l2[j:]):
                    arr[k] = v
                    k+=1
                break
            if len(l2)==j:
                for l,v in enumerate(l1[i:]):
                    arr[k] = v
                    k+=1
                break
            else:
                if l1[i]<=l2[j]:
                    arr[k] = l1[i]
                    i+=1
                    k+=1
                elif l1[i]>=l2[j]:
                    arr[k] = l2[j]
                    j+=1   
                    k+=1


if __name__ == '__main__':
    array = [4, 2, 3, 8, 8, 43, 6,1, 0]
    merge_sort(array)
    print(array)            