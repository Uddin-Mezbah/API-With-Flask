""" creat CRUD"""
######################################
#                                    #
# MD MEZBAH UDDIN                    #
# Nantong University(China)          #
# CSE                                #
#                                    #
######################################

from flask import Flask,request

database = {'uddin': '100'}

#intialize flask app
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    # return "Welcome to my web api"
    # return "Welcome to my web api"
    return '<h1>Hello, Uddin!</h1>'
# @app.route('/something',methods=['GET'])
# def onno_kichu():
#     return "mathai ki r kichu nai"

@app.route('/getdata',methods=['GET'])
def get_data():
    return database

@app.route('/adddata',methods=['GET','PUT'])
def add_data():
    key,value = list(request.args.items())[0]
    database[key] = value
    return f'{key} added'

if __name__ == '__main__':
    app.run()
