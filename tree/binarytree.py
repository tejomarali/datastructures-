" Construct a binary tree and perform various various."


def binarysearch(array,x):  
    low=0  
    high=len(array)-1  
    mid = 0  
    while low<=high:  
        mid=(low+high)//2  
        if array[mid] <x:  
            low=mid+1  
        elif array[mid]>x:  
            high=mid-1  
        else:  
            return mid  
    return -1  
array=[3,6,7,8,10,12,13,17,19]  
x=7
res=binarysearch(array,x)  
if res!=-1:  
    print("Element is present at index", str(res))  
else:  
    print("Element is not present in the array")  
    
    
OUTPUT:-
Element is present at index 2
