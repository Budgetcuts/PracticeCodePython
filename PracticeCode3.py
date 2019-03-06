def removeVowels(s):
    vowels = "AEIOUaeiou"
    newString = ""
    for c in s:
        if c not in vowels:
            newString += c
    return newString

class Point
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x) + "," + str(self.y)

def main():
    accum = ""
    for i in range(1,1000):
        accum = accum + str(i) + ","
    accum +="1000"
    print(accum)

    b = "Binghamton"
    print(b[:3])
    print(b[4:6] + b[-3])
    print(b[:2] + b[-3] + b[1:4])

    results = 'average: 0.8475'
    index = results.find(" ")
    num = results[index:]
    num = float(num)
main()
