from flask import Blueprint, Response

from .data_collectors import fetch_cpu, fetch_storage,fetch_summary

api = Blueprint('api', __name__)

@api.route('/')
def summary():
    data = fetch_summary()
    return  Response(data)