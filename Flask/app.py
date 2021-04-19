from flask import Flask
import automated_accessibility_testing

app = Flask(__name__)

@app.route("/")


with open("colortest.html", "r", encoding='utf-8') as f:
    text= f.read()

aat_res = automated_accessibility_testing.check_accessibility(text)

def hello():
    return "Hello, World!"
    for x in range(0,len(aat_res)-1):
        return(aat_res[x])
