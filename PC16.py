class WrongAnswerError(Exception):
    pass

class NoAnswerError(Exception):
    pass

def main():
    Food = "Calamari"
    ans = input("What is your favorite food ")
    while (Food != ans):
        try:
            if(ans ==""):
                raise NoAnswerError
            elif(ans != Food):
                raise WrongAnswerError
        except NoAnswerError:
            print("Please enter an answer:")
            ans = input("What is your favorite food? ")
        except WrongAnswerError:
            print("Wrong, the correct answer is Calamari")
            ans = Food
        else:
            print("Congrats on the impeccable taste")

main()
