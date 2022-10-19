def FizzBuzz( n ):
    a = []
    for i in range(1,n+1):
        if i % 4 == 0 and i % 6 == 0:
            a.append('FizzBuzz')
        elif i % 4 == 0:
            a.append('Fizz')
        elif i % 6 == 0:
            a.append('Buzz')
        else:
            a.append(i)
    return a



if __name__=='__main__':
    x = FizzBuzz( 13 )
    print( x )
