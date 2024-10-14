def binary_search(l, key):
    low = 0
    mid = len(l) // 2
    high = len(l) - 1

    while low <= high:
        if key == l[mid]:
            print("Number found at index", mid)
            quit()
        else:
            if key < l[mid]:
                high = mid - 1
            else:
                low = mid + 1
                
            mid = (low + high) // 2
        
    print("Number not found")

n= int(input("Enter size "))
l = []
for i in range(n):
    num = int(input("Enter number "))
    l.append(num)
    
l.sort()    
key = int(input("Enter the number to search for "))
binary_search(l, key)