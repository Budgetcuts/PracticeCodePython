def main():
    #reading, file must exist
    x = input("What's the file's name? ")
    fo = open(x, "r")
    accum = ""
    for i in fo.read():
        if(i.isalnum()):
            accum += chr(ord(i) + 7)
        else:
            accum += i

    #writing, truncates and writes, file may or may not exist
    #fo = open("myFile.txt", "w")
    #appending, adds to the file, file may or may not exist
    #fo = open("myFile.txt", "a")

    fo.close()

    fo = open(x + ".enc", "w")
    fo.write(accum)
    fo.close()
main()
