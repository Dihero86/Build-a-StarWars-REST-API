from flask import Flask, jsonify

def response_error(msg, status_code):
    return({
        'msg':msg,
        'error' : True
    }),status_code

def response_ok(data,status_code):
    return jsonify(data),status_code