def main():
     ThisList = []
     Proc = True
     x = "0"
     while (Proc == True):
         x = input("Please enter a positive integer, to end the list input a negative number:")
         if (int(x) > 0):
             ThisList.append(int(x))
         else:
             Proc = False
     return ThisList
     print(len(ThisList))
main()
