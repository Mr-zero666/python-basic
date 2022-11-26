def Dectobin(input):
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

if __name__ == '__main__':
    r = Dectobin(32)
    print(r)

