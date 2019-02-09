def binarysearch(mylist,target):
    left = 0
    right = len(mylist)
    steps = 0
    while (left < right-1):
        steps = steps + 1
        mid = int((right+left)/2)
        number_at_mid = mylist[mid]
        print("Steps taken to find the number: ",steps)
        if (target == number_at_mid):
            return True
        if (target < number_at_mid):
            right = mid
        else:
            left = mid
        if (left >= right):
            return False
        if ( (left == (right-1)) and (mylist[left] == target) ):
            return True
    
    return False
    
mylist = [11,27,36,44,51,22,65,1,78]
print (mylist)
mylist.sort()
print (mylist)
 
repeat = "y"
while (repeat == "y" or repeat == "Y"):
    mytarget = int(input("Enter number to find: "))
    if binarysearch(mylist,mytarget):
        print ("Found!")
    else:
        print ("NOT Found!")
    repeat = input("Another search? (y/n)")
print ("\n\nThank you for using this program")

