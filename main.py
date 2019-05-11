"""
    author: Himesh Buch
    topic: Principles of Programming Language- Final Project
    date: 5/12/2019
    
"""



#importing packages (not all of them are installed by default)
import sys
import time
import subprocess
import os
from flask import Flask, render_template, request, session, redirect, url_for
from threading import Thread
import random, json
import requests
import datetime
from bs4 import BeautifulSoup

try: 
    import urllib.request as urllib2
    from googlesearch import search 
except ImportError:  
    import urllib2
    print("No module named 'google' found") 

app = Flask(__name__)
now = datetime.datetime.now()

#using lists to store data locally, mainly to display it on webpages. we are also storing data in .txt files
#dictionaries could have been used, but lists seem to be an easier option
date = []
header = []
link = []
bl = []
results = []
titles = []
resultsPdf = []
titlesPdf = []
ind = []
threads = []
threadsPdf = []
detailsExtra = []
details = []


#reading titles from the database
def data_title():
    with open('data_titles.txt', 'a') as f:
        for item in ind:
            f.write("%s\n" % item)

#reading url of different search results from the database
def data_url():
    with open('data_url.txt', 'a') as f:
        for item in bl:
            f.write("%s\n" % item)

#main algorithm which generates url search results
def res(q):
    query = q
    for j in search(query, tld="com", num=6, stop=6, pause=2): 
        results.append(j)
        
        #using beautifulsoup package to scrape the webpage
        detailss(results[len(results)-1])
        r = requests.get(j).text
        soup = BeautifulSoup(r, 'html.parser')
        
        #saving titles
        if len(soup.title.string) > 50:
            titles.append(soup.title.string[0:45] + "...")
        else:
            titles.append(soup.title.string)
    
    #saving history
    for i in range(0, len(results)):   
        history1(now.strftime("%Y-%m-%d"), str(now.hour)+":"+str(now.minute), results[i], titles[i])
    return results
    
    
#to generate pdf search results
def resPdf(q):
    query = q + " pdf"
    for j in search(query, tld="com", num=6, stop=6, pause=2): 
    
        #scraping a pdf was out of scope for this project. instead, we get some part of the url and 
        #display it as title
        if j[-3:] == "pdf":
            resultsPdf.append(j)
            titlesPdf.append(j.split('/')[2])
            
    
    #saving history
    for i in range(0, len(results)):   
        history1(now.strftime("%Y-%m-%d"), str(now.hour)+":"+str(now.minute), results[i], titles[i])
    return resultsPdf


#generating details of the search term
def detailss(q):
    try:
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
    except ConnectionError:
        details.append("")


#saving previously browsed results in the database
def history1(d,t,l,title):
    with open('history.txt', 'a') as f:
        x = str(d + "*" + t + "*" + l + "*" + title)
        f.write("%s\n" % x)
   
   
#routes     
@app.route('/')
def mainPage():
    return render_template("main.html", results = [], url = [], c = 0, details = [])
    
#bucketList page
@app.route('/bucketList', methods=['GET','POST'])
def bucketLists():

    #reading from the database
    with open('data_url.txt') as f:
        bl = f.read().splitlines()
    with open('data_titles.txt') as f:
        ind = f.read().splitlines()
    return render_template("bucketList.html", bl = bl, url = ind, c = len(bl))
    
    
#adding items to bucketList
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


#url page (displays url search results)
@app.route('/url', methods=['GET','POST'])
def url():
    details.clear()
    results.clear()
    titles.clear()
    resultsPdf.clear()
    titlesPdf.clear()
    a = request.args.get('a')
    
    """
        we generate url results in two steps. 
            1) getting the search term (/urls)
            2) passing that term to the main algorithm (/url)
        since we have multiple routes to perform these tasks, we need to wait until the results
        are sent back from the search algorithm. we use threading for that, which stops all the processes
        until the results are sent back
        
    """
    for i in range(0,1):
        process = Thread(target=res, args=[a])
        process.start()
        threads.append(process)
    for process in threads:
        process.join()
    return "ok"
    
@app.route('/urls', methods=['GET','POST'])
def urls():

    #getting the search term. we use ajax for that
    for process in threads:
        process.join()
    return render_template("main.html", results = titles, url = results, details=details, c = len(results))

#same logic for pdf search results
@app.route('/pdf', methods=['GET','POST'])
def pdf():
    details.clear()
    resultsPdf.clear()
    titlesPdf.clear()
    results.clear()
    titles.clear()
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

    #getting the search term. we use ajax for that
    for process in threadsPdf:
        process.join()
    return render_template("main.html", results = titlesPdf, url = resultsPdf, details=[], c = len(resultsPdf))
    
#passing history response back to html
@app.route('/history', methods=['GET','POST'])
def history():
    date.clear()
    link.clear()
    header.clear()
    with open('history.txt') as f:
        num = sum(1 for line in f)
    with open('history.txt') as f:
        print(num)
        x = f.read().splitlines()
        for i in range(0,num):
            date.append(str(x[i].split("*")[0]) + " " + str(x[i].split("*")[1]))
            link.append(x[i].split("*")[2])
            header.append(x[i].split("*")[3])
    return render_template("history.html", date = date, title = header, url = link, c = len(header))
    
    
if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
