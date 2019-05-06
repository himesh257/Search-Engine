import sys
import time
import subprocess
import os
from flask import Flask, render_template, request, session, redirect, url_for
from threading import Thread
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

carss = ['honda', 'hundai', 'toyota','o','o']
bl = []
results = []
titles = []
resultsPdf = []
titlesPdf = []
ind = []
timess = []
threads = []
threadsPdf = []
detailsExtra = []
details = []
pTag = []

def data_title():
    with open('data_titles.txt', 'a') as f:
        for item in ind:
            f.write("%s\n" % item)

def data_url():
    with open('data_url.txt', 'a') as f:
        for item in bl:
            f.write("%s\n" % item)

def res(q):
    query = q
    for j in search(query, tld="com", num=3, stop=2, pause=3): 
        results.append(j)
        detailss(results[len(results)-1])
        r = requests.get(j).text
        soup = BeautifulSoup(r, 'html.parser')
        if len(soup.title.string) > 50:
            titles.append(soup.title.string[0:45] + "...")
        else:
            titles.append(soup.title.string)
    end = time.time()
    return results
    
def resPdf(q):
    query = q + " pdf"
    for j in search(query, tld="com", num=3, stop=2, pause=2): 
        if j[-3:] == "pdf":
            resultsPdf.append(j)
            titlesPdf.append(j.split('/')[2])
    return resultsPdf

def detailss(q):
    soup = BeautifulSoup(requests.get(q).text, 'lxml')
    for h in soup.find_all(["h1", "h2", "h3", "h4", "h5"]):
        x = str(h.text.strip())
        detailsExtra.append(x)
    y = ' '.join(detailsExtra)
    if len(y) > 155:
        d = y[0:150]+"...."
        details.append(d)
        detailsExtra.clear()
    else:
        details.append(y)
        detailsExtra.clear()

@app.route('/')
def mainPage():
    return render_template("main.html", results = [], url = [], c = 0, details = [])
    #return render_template("main.html", results = carss, url = url, c = len(carss), details=details)
    
@app.route('/bucketList', methods=['GET','POST'])
def bucketLists():
    with open('data_url.txt') as f:
        bl = f.read().splitlines()
    with open('data_titles.txt') as f:
        ind = f.read().splitlines()
    return render_template("bucketList.html", bl = bl, url = ind, c = len(bl))
    
@app.route('/final')
def addBtn():
    a = request.args.get('a')
    bl.append(a)
    data_url()
    if a in results:
        i = results.index(a)
        ind.append(titles[i])
        data_title()
    else:
        i = resultsPdf.index(a)
        ind.append(titlesPdf[i])
        data_title()
    return "ok"

@app.route('/url', methods=['GET','POST'])
def url():
    a = request.args.get('a')
    for i in range(0,1):
        process = Thread(target=res, args=[a])
        process.start()
        threads.append(process)
    for process in threads:
        process.join()
    return "ok"
    
@app.route('/urls', methods=['GET','POST'])
def urls():
    for process in threads:
        process.join()
    return render_template("main.html", results = titles, url = results, details=details, c = len(results))

@app.route('/pdf', methods=['GET','POST'])
def pdf():
    a = request.args.get('a') 
    for i in range(0,1):
        process = Thread(target=resPdf, args=[a])
        process.start()
        threadsPdf.append(process)
    for process in threadsPdf:
        process.join()
    return "ok"
    
@app.route('/pdfs', methods=['GET','POST'])
def pdfs():
    for process in threadsPdf:
        process.join()
    return render_template("main.html", results = titlesPdf, url = resultsPdf, details=[], c = len(resultsPdf))
    
if __name__ == '__main__':
    app.run(debug=True)
