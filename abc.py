import sys, os
from html import escape
from flup.server.fcgi import WSGIServer
import requests
from bs4 import BeautifulSoup
import webbrowser
import time
import re


def build():
    url = 'https://www.mrtechsonu.com/free-google-play-redeem-code-gift-card'
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')

    text = soup.find_all(text=True)
    text += soup.find_all('td')
    text += soup.find_all('tr')
    text += soup.find_all('li')

    file2 = open("MyFile.txt", "r")
    text2 = file2.read()
    file1 = open("MyFile.txt", "a")

    output = []
    for t in text:
        p = t.string
        if p == None:
            continue
        op = ''
        for i in p:
            if i not in (' ', '/', '{', ':', '}', ')', ']', '=', None):
                op += i
            else:
                op = ''
        if len(op) > 15:
            if p not in text2:
                output.append(op)
                file1.write(p + '\n')
    yield f"*[str(j) + '.  ' + i + '\n' for j, i in enumerate(output)];"
    for op in output[::-1]:
        url = 'https://play.google.com/store?code=' + op
        webbrowser.open(url, 2, False)
        time.sleep(13)

    file1.close()
    file2.close()
    yield "done!!!"


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    build()


WSGIServer(app).run()
