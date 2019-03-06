




def foo():
    num = int(input("Please enter a number greater than 5"))
    if(num < 6):
        raise Exception()
    else:
        print("Great Job")

def main():
    try:
        fptr = open("myFile.txt", "r")
    except FileNotFoundError as err:
        fptr = open("myFile.txt","w")
    else:
        print("else")

#    try:
#        val = int(textnum)
#    else:
#        print("only if no error")
#    finally:
#        fptr.close()

#    with open("myFile.txt") as fptr:
#        print(fptr.read())
    try:
        foo()
    except:
        print("error")
main()
