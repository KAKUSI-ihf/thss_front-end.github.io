# from crypt import methods
from requests import request
from mod2 import app
from flask import render_template, request, redirect,url_for
import random

current = {
    'id': '',
    'traffic': 0.0
}
dic = dict()

@app.route('/')
def index():
    return render_template(
        'index.html'
    )

@app.route('/login',methods=['POST'])
def login():
    user_id = request.form['user_id']
    if user_id not in dic:
        dic[user_id] = 0.0
    else:
        dic[user_id] = dic[user_id] + random.uniform(0,10)
    current['id'] = user_id    
    current['traffic'] = dic[user_id]
    return redirect(url_for('connected'))

@app.route('/connected.html')
def connected():
    current_show = dict()
    current_show['id'] = current['id']
    current_show['traffic'] = '{:.2f}'.format(current['traffic']) + 'G'
    return render_template(
        'connected.html',
        current_user = current_show
    )

@app.route('/disconnect')
def disconnect():
    return redirect(url_for('index'))