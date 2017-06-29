from flask import Flask
from pymongo import MongoClient
from flask import jsonify, render_template, request
from flask_socketio import SocketIO
from flask_socketio import send, emit
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
socketio.run(app, host='0.0.0.0')

# if __name__ == '__main__':
#     socketio.run(app)

@socketio.on('connect')
def socketio_connect():
    print "socketio_connect"

@app.route("/get")  # one route accounts for only one "return" result
def myDict():
    client = MongoClient("mongodb://zilinwang:Mongo0987654321@129.59.107.60:27017/fire_department")
    db = client["fire_department"]["incident"]
    items = db.find()
    dictOut = {}
    dictArr = []
    dictOut['incidents']=dictArr

    for item in items:
        dictIn = {}
        dictIn['_id'] = str(item['_id'])
        dictIn['incidentNumber'] = item['incidentNumber']
        dictIn['_lat'] = item['latitude']
        dictIn['_lng'] = item['longitude']
        dictIn['year'] = item['year']
        dictIn['month'] = item['month']
        dictIn['day'] = item['calendarDay']
        dictIn['alarmDate'] = item['alarmDateTime']
        dictIn['closestStation'] = item['closestStation']
        dictIn['severity'] = item['severity']
        dictIn['streetNumber'] = item['streetNumber']
        dictIn['streetPrefix'] = item['streetPrefix']
        dictIn['streetName'] = item['streetName']
        dictIn['streetType'] = item['streetType']
        dictIn['streetSuffix'] = item['streetSuffix']
        dictIn['apartment'] = item['apartment']
        dictIn['city'] = item['city']
        dictIn['county'] = item['county']
        dictIn['state'] = item['state']
        dictIn['zipCode'] = item['zipCode']

        dictArr.append(dictIn)

    return jsonify(dictOut)

    # print dictArr[1]
    # r = json.dumps(dictOut)
    # loaded_r = json.loads(r)

# myDict()
