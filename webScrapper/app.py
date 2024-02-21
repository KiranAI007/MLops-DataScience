from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import logging

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def homepage():
    return render_template("index.html")

@app.route("/review", methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content']
            flipKart_url = "https://www.flipkart.com/search?q=" + searchString
            uClient = uReq(flipKart_url)
            flipKartPage = uClient.read()
            uClient.close()
            flipkart_html = bs(flipKartPage,"html.parser")
        except Exception as e:
            print(e)

if __name__ =='__main__':
    app.run(host='0.0.0.0')