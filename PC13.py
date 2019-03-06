import json
#json formatted strings, not files
def main():
    fptr = open("people.json")
    data = fptr.read()
    fptr.close()
    print(type(data), data)
    pdata = json.loads(data)
    print(type(pdata), data)
    pdata["Friends"].append("Dread Pirate Roberts")
    pdata = json.dumps(pdata)
    print(type(pdata), data)
    fptr = open("people.json", "w")
    data = fptr.write(pdata)
    fptr.close()
main()
