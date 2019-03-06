import requests
from PIL import Image
from io import BytesIO

def main():
    try:
        contents = requests.get("https://aws.random.cat/meow")
    except:
        print("Something went wrong")
    else:
        img = Image.open(BytesIO(contents.content))

main()
