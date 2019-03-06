import requests

def main():
    try:
        contents = requests.get("http://opentdb.com/api.php?amount=1&category=18")
    except:
        data = ""
    else:
        data = contents.json()
    trivia = data['results'][0]
    print(trivia['question'])
    print(trivia['correct_answer'])
main()
