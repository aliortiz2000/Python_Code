# Implementation of binary search algorithm!!

# We will prove that binary search is faster than naive search!


# Essence of binary search:
# If you have a sorted list and you want to search this array for something,
# You could go through each item in the list and ask, is this equal to what we're looking for?
# But we can make this *faster* by leveraging the fact that our array is sorted!
# Binary search ~ O(log(n)), naive search ~ O(n)

# In these two examples, l is a list in ascending order, and target is something that we're looking for
# Return -1 if not found

def native_search (l, target) :
    for item in range (len (l)): 
        if l [item] == target :
            return item
    return -1
    
    
# Binary search uses divaide and conquer
# We will leverage the fact that our list is sorted    
def binary_search (l, target, low = None, high = None) :
    
    # Initial data arrangement
    if low == None :
        low = 0
    if high == None : 
        high = len (l) -1
    
    # The target is not on the list 
    if high < low : 
        return -1
    
    midpoint = ( low + high ) // 2 
        
    if l [ midpoint ] == target :
        return midpoint # When the target is on the list 
    elif l [ midpoint ] < target :
        return binary_search ( l, target, midpoint+1 , high )
    else : 
        # item > target 
        return binary_search ( l, target, low, midpoint-1)
    
    
if __name__=='__main__':
    l = [1, 3, 5, 9, 11, 12, 15, 18, 20, 25, 29, 36]
    target = 9
    print ( native_search ( l, target ) )
    print ( binary_search ( l, target ) )