#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:42:02 2018

@author: takanori
"""

from flask import Flask
from flask import render_template, request #追加
from flask import json,Response,jsonify
from sklearn.externals import joblib



app = Flask(__name__)


def jsonp(data, callback="function"):
    return Response(
        "%s(%s);" %(callback, json.dumps(data)),
        mimetype="text/javascript"
        )

def dicide(data):
    ansary=['not defined','あ','い','う','え','お']
    
    clf = joblib.load('./clf.pkl') 
    number = clf.predict([data])
    answer = int(number[0])
    
    return ansary[answer] 
    


@app.route('/')
def index():
    print("OK")
    return 'connection is fine'

@app.route('/test',methods=['GET','POST'])
def test(*args,**kwargs):
    
    callback = request.args.get('callback',False)
    print("--------")
    print(request.args.getlist("dataAry[]"))
    print("--------")
    
    if callback:
        if request.method =='POST':
            return jsonp("Method 'POST' is not arrowed",callback)
        else:
            data = request.args.getlist("dataAry[]")
            val = dicide(data)
            
            return jsonp(val,callback)

    return callback+"(HELLO)"


if __name__== '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=8080)