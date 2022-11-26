def StringToNumber(s):
    if s.isdigit():
        a = int(s)
    else:
        a = float(s)
    return a

if __name__ == '__main__':
    x = StringToNumber('12345.123')
    print(x)
