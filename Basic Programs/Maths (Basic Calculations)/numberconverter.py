# Convert Decimal to Binary, Octal and Hexa
def print_formatted(number):
    for x in range(1,number+1):
        #print("{0:b}".format(x)) Binary
        #print("{0:o}".format(x)) Octal
        #print("{0:x}".format(x)) Hexa
        print(str(x)+" "+"{0:o}".format(x)+" "+"{0:x}".format(x)+" "+"{0:b}".format(x))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
