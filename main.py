import sys
import time
import subprocess
import os
from flask import Flask, render_template, request, session, redirect, url_for
import random, json
import requests
from bs4 import BeautifulSoup

try: 
    import urllib.request as urllib2
    from googlesearch import search 
except ImportError:  
    import urllib2
    print("No module named 'google' found") 

app = Flask(__name__)
app.secret_key = os.urandom(24)

carss = ['honda', 'hundai', 'toyota','o','o']
bl = []
results = []
titles = []
resultsPdf = []
titlesPdf = []
ind = []

def data_title():
    with open('data_titles.txt', 'w') as f:
        print(ind)
        for item in ind:
            f.write("%s\n" % item)


def data_url():
    with open('data_url.txt', 'w') as f:
        for item in bl:
            f.write("%s\n" % item)

def res(q):
    start = time.time()
    query = q
    for j in search(query, tld="com", num=2, stop=1, pause=3): 
        #print(j)
        results.append(j)
        r = requests.get(j).text
        soup = BeautifulSoup(r, 'html.parser')
        if len(soup.title.string) > 50:
            titles.append(soup.title.string[0:45] + "...")
        else:
            titles.append(soup.title.string)
    print(results)
    end = time.time()
    return results
    
def resPdf(q):
    query = q + " pdf"
    for j in search(query, tld="com", num=3, stop=5, pause=2): 
        print(j)
        if j[-3:] == "pdf":
            resultsPdf.append(j)
            titlesPdf.append(j.split('/')[2])
       
    print(resultsPdf)
    print(titlesPdf)
    return resultsPdf


@app.route('/')
def mainPage():
    print("im at mainpage")
    
    a = request.args.get('a')
    return render_template("main.html", results = [], url = [], c = 0)
    #return render_template("main.html", results = carss, url = url, c = len(carss))
    
@app.route('/bucketList', methods=['GET','POST'])
def bucketLists():
    print('bl page')
    with open('data_url.txt') as f:
        bl = f.read().splitlines()
    with open('data_titles.txt') as f:
        ind = f.read().splitlines()
    print(bl)
    print(ind)
    return render_template("bucketList.html", bl = bl, url = ind, c = len(bl))
    
@app.route('/final')
def addBtn():
    a = request.args.get('a')
    bl.append(a)
    data_url()
    if a in results:
        i = results.index(a)
        ind.append(titles[i])
        print(ind)
        data_title()
    else:
        i = resultsPdf.index(a)
        ind.append(titlesPdf[i])
        print(ind)
        data_title()
    print(bl)
    print(ind)
    return "ok"

@app.route('/url', methods=['GET','POST'])
def url():
    print('url page')
    a = request.args.get('a') 
    res(a) 
    return "ok"
    
@app.route('/urls', methods=['GET','POST'])
def urls():
    time.sleep(7)
    print(results)
    return render_template("main.html", results = titles, url = results, c = len(results))

@app.route('/pdf', methods=['GET','POST'])
def pdf():
    print('pdf page')
    a = request.args.get('a') 
    resPdf(a) 
    print("--------------")
    print(resultsPdf)
    print(titlesPdf)
    return "ok"
    
@app.route('/pdfs', methods=['GET','POST'])
def pdfs():
    time.sleep(7)
    print(results)
    return render_template("main.html", results = titlesPdf, url = resultsPdf, c = len(resultsPdf))


    
if __name__ == '__main__':
    app.run(debug=True)
