from flask import Blueprint, Response,render_template 

from .data_collectors import fetch_cpu, fetch_storage,fetch_summary

import json

api = Blueprint('api', __name__)

@api.route('/')
def summary():
    data = fetch_summary()
    return  Response(data)


@api.route('/test')
def info():
    raw_json = fetch_summary()
    data = json.loads(raw_json)
    return render_template('index.html', data=data)