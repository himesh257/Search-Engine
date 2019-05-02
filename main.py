import sys
from flask import Flask, render_template, request, jsonify
import random, json

app = Flask(__name__)

carss = ['honda', 'hundai', 'toyota']
url = ["http://www.google.com", "https://www.google.com/search?q=bootstrap+footers&oq=boo&aqs=chrome.0.69i59j69i60j69i65l2j69i57j69i59.799j0j7&sourceid=chrome&ie=UTF-8", "https://getbootstrap.com/docs/4.1/examples/"]
bl = [];


@app.route('/')
def mainPage():
    print("im at mainpage")
    return render_template("main.html", results = carss, url = url, c = len(carss))

@app.route('/bucketList', methods=['GET','POST'])
def bucketLists():
    print('bl page')
    return render_template("bucketList.html", bl = bl, c = len(bl))
    
@app.route('/final')
def addBtn():
    a = request.args.get('a')
    bl.append(a)
    print(bl)
    return a
    
@app.route('/pdf')
def pdf():
    a = request.args.get('a')
    print(a)
    return a
    
@app.route('/url')
def url():
    a = request.args.get('a')
    print(a)
    return a
    
    
    
 
    
if __name__ == '__main__':
    app.run(debug=True)
