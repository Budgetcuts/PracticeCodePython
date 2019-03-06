def foo(array):
    array[0] = 10
    return array
def main():
    mylist = [1, "2", 3.0] + [4,5,6]
    foo(mylist)
    mylist[3:3] = [3]
    del(mylist[3])
    print(mylist)
main()
