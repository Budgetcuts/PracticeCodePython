def sum_of_squares(xs):
    TotVal = 0
    for i in range(len(xs)):
        TotVal+= (int(xs[i]))**2
    print(TotVal)



def main():
    a = [1,2,3]
    a.append("apple")
    a.append(76)
    a.insert(0,99)
    a.insert(2, "cat")
    n = 0
    for i in range(len(a)):
        if (a[i] == 76):
            n+=1
    print(n)
    for i in range(len(a)):
        if (a[i] == 76):
            a.remove(76)
            break
    a.remove("apple")
    a.insert(5, "orange")
    sum_of_squares([1,2,3])


main()
