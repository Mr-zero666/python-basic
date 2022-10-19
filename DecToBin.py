def DecToBin( n ):
    out = list()
    new = ''
    while input != 0:
        t = input % 2
        out.append(str(t))
        input = int(input/2)
        if input == 1:
            out.append(str(input))
            break
    out.sort(reverse=True)
    new = new.join(out)
    return new
    


if __name__=='__main__':
    s = DecToBin( 32 )
    print( s )
