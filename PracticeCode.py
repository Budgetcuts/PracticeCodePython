
import random
def isCorrect():
        num = int(random.randint(0,11))

        for i in range(3):
            numGuess = int(input("Please guess the number:"))
            if(numGuess<num):
                print("Too low!")
                continue
            elif(numGuess>num):
                print("Too high!")
                continue
            else:
                print("Correct!")
                break

def Grade():
    RealGrade = int(input("Input your exam grade:"))
    if (RealGrade >= 90)
        print("Good job you got an A!")
    elif(RealGrade =>80)
        print("Nice going you got a B!")
    elif(RealGrade =>70)
        print("Your performance is questionable, you recieved a C.")
    elif(RealGrade =>60)
        print("Everything okay at home? You got a D.")
    elif(RealGrade >0)
        print("Why?")
def main():
    isCorrect()
main()
