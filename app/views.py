#!/home/info/env/bin/python3.6
# -*- coding:utf-8 -*-
#import os, json, re
#from werkzeug import secure_filename
from flask import render_template, flash, redirect, session, url_for, request, g
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title = 'Info AlwaysData')
