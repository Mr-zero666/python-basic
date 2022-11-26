def IsSame( a ): #check list has same numbers
    n = len(a)
    e = a[0]
    same = 1
    for i in range( 1, n ):
        if a[i] != e:
            same = 0
            break # no need to loop any more

    return same

def DetermineOrder( a ): # a is a sorted list
    n = len( a )
    order = None
    
    if a[0] < a[n-1]: order = 'asc'
    elif a[0] > a[n-1]: order = 'desc'
    else:
        pass

    return order


def MergeSorted( l1, l2 ):
    same1 = IsSame(l1)
    same2 = IsSame(l2)

    r = []
    r.extend( l1 )
    r.extend( l2 )

    if same1==1 and same2==1:
        r.sort()
    elif same1 == 1:
        order = DetermineOrder( l2 )
        if order == 'asc':
            r.sort()
        elif order == 'desc':
            r.sort( reverse = True )
        else:
            r.sort() # just sort
            
    elif same2 == 1:
        order = DetermineOrder( l1 )
        if order == 'asc':
            r.sort()
        elif order == 'desc':
            r.sort( reverse = True )
        else:
            r.sort()
    else:
        order = DetermineOrder( l1 )
        if order == 'asc':
            r.sort()
        elif order == 'desc':
            r.sort( reverse = True )
        else:
            r.sort()
        
    return r            





if __name__=='__main__':
    #l1 = [ 1, 22, 333, 4444, 55555]
     
    #l2 = [ 3, 44, 111, 222, 666]
    l1 = [1, 1, 1]
    l2 = [8, 7, 6]

    l = MergeSorted( l1, l2 )
    print( l )
