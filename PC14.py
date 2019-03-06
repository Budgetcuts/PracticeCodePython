import json

def main():
    news = open("Article.txt").read()
    subs = json.load(open("substitution.json"))

    for keys in subs:
        news = news.replace(keys, subs[keys])
    fptr = open("betternews.txt","w")
    fptr.write(news)
    fptr.close()

main()
