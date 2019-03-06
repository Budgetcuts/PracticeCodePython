#def main():

#    contacts = {"Luke":"123", "Leia":"456", "Han":"789"}

#    name, number = input("Please input a name:"), input("Please enter a number")
#    contacts ["Han"] = "354"
#    contacts["Chewie"] = "460"
#    contacts[name] = number
#    print(contacts)

    #del contacts ["Han"]
#    keys = contacts.keys()
#    vals = contacts.values()
#    print (contacts.get("Luke", "Name not found"))

#main()

def main():

    mystring = "Hello"
    char_frequency = {}
    for c in mystring:
        char_frequency[c] = mystring.count(c)
    char_frequency = {c : mystring.count(c)
        for c in mystring}

    print(char_frequency)
main()
