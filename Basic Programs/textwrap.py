# Program to test Textwrap
import textwrap

def wrap(string, max_width):
    #a = textwrap.wrap(string,max_width) #returns a list
    return textwrap.fill(string, max_width) # returns string by string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
