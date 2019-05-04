import sys
import time
import os
from flask import Flask, render_template, request, session, redirect, url_for
import random, json
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 

app = Flask(__name__)
app.secret_key = os.urandom(24)
#carss = ['honda', 'hundai', 'toyota']
#url = ["http://www.google.com", "https://www.google.com/search?q=bootstrap+footers&oq=boo&aqs=chrome.0.69i59j69i60j69i65l2j69i57j69i59.799j0j7&sourceid=chrome&ie=UTF-8", "https://getbootstrap.com/docs/4.1/examples/"]
bl = [];
results = [];
resultsUrl = [];
one = '' 
 
def res(q):
    query = q
    for j in search(query, tld="co.in", num=1, stop=2, pause=2): 
        #print(j)
        results.append(j)
    return results
    
def resUrl(q):
    query = q
    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        #print(j)
        resultsUrl.append(j)
    return resultsUrl


@app.route('/')
def mainPage():
    print("im at mainpage")
    a = request.args.get('a')
    #return render_template("main.html", results = res(a), url = url, c = len(x))
    return render_template("main.html", results = [], url = url, c = 0)
    
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

@app.route('/pdf', methods=['GET','POST'])
def pdf():
    start = time.time()
    print('pdf page')
    a = request.args.get('a')   
    print(res(a))
    print(results)
    end = time.time()
    one = end - start
    #print(end - start)
    return "ok"
    
    
@app.route('/pdfs', methods=['GET','POST'])
def pdfs():
    time.sleep(4)
    return render_template("main.html", results = results, url = results, c = len(results))

@app.route('/url')
def url():
    print('url page')
    a = request.args.get('a')   
    print(resUrl(a))
    print(resultsUrl)
    return "ok"
    
@app.route('/urls', methods=['GET','POST'])
def urls():
    print(results)
    return render_template("main.html", results = resultsUrl, url = results, c = len(resultsUrl))

    
 
    
if __name__ == '__main__':
    app.run(debug=True)
