def ReverseDigits(n):
    s = ''
    new_list = list(str(n))
    for i in range(len(new_list)):
        if new_list[-1] == '0':
            new_list.pop()
    t = new_list[::-1]
    for item in t:
        s = s+item
    return int(s)

if __name__ == '__main__':
    n = ReverseDigits(123)
    print(n)