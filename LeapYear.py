def IsLeapYear( y ):
       if (y % 4 == 0 and y % 100 != 0) or  y % 400 == 0:
        return True



if __name__=='__main__':
    r = IsLeapYear( 2020 )
    print ( r )
    assert r == True
