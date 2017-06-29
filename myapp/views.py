from myapp import app
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, send, emit
from myapp import socketio

@app.route('/')
@app.route('/index')
def index():
    print "-> index()"
    return render_template("socket.html")


@socketio.on('connect')
def socketio_connet():
    print "-> socketio_connet()"