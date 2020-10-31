def Bsearch(key,lst):
    low=0
    high=len(lst)-1
    while low<=high: 
        mid=(high+low)//2  # Getting middle value in array 
        if lst[mid]==key:
            return mid
        elif key<lst[mid]: # if key<middle element means higher index needs
            #to be modified as right side wasted 
            high=mid-1
        else: #if key>middle element means left side waste and lower index needs
            #to be  modified as mid+1
            low=mid+1
    else:
        return -1
lst=[1,23,45,67,90,20,40]
lst.sort()
print("Sorted list :",lst)
key=int(input("Enter value to be search in array :"))
a=Bsearch(key,lst)
if a==-1:
    print("Element not foiund in array")
else:
    print(f'Element found at position {a+1}')
