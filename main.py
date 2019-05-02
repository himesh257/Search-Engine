import sys
from flask import Flask, render_template, request, jsonify
import random, json

app = Flask(__name__)

carss = ['honda', 'hundai', 'toyota']
url = "http://www.google.com"

@app.route('/')
def mainPage():
    print("im at mainpage")
    return render_template("main.html", results = carss, url = url, c = len(carss))
    
#@app.route('/b')
#def bucketListss():
#    print('bl page')
#    return render_template("bucketList.html", cars = carss, c = len(carss), url = url)

@app.route('/bucketList', methods=['GET','POST'])
def bucketLists():
    print('bl page')
    if request.method == 'POST':
        return render_template("bucketList.html")
    return render_template("bucketList.html")
    
@app.route('/final')
def addBtn():
    a = request.args.get('a')
    print(a)
    return a
    
    
    
 
    
if __name__ == '__main__':
    app.run(debug=True)
