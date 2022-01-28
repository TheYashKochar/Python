# Program using String Validators
if __name__ == '__main__':
    s = input()
    print(any([a.isalnum() for a in s]))
    print(any([a.isalpha() for a in s]))
    print(any([a.isdigit() for a in s]))
    print(any([a.isupper() for a in s]))
    print(any([a.islower() for a in s]))
    '''
    print(s.isalnum())
    print(s.isalpha())
    print(s.isdigit())
    print(s.isupper())
    print(s.islower())'''
    '''isal = 0
    isalnu =0
    isdig =0
    isup = 0
    islow = 0
    for x in s:
        if x.isalpha():
            isal = 1
        if x.isdigit():
            isalnu = 1
        if x.isalnum():
            isdig = 1
        if x.isupper():
            isup = 1
        if x.islower():
            islow = 1

    #print(isalnu + "\n" +isal + "\n" +isdig + "\n" +isup + "\n" +islow + "\n")
    print(isal)    '''
