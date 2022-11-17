"""My creat api"""
######################################
#                                    #
# MD MEZBAH UDDIN                    #
# Nantong University(China)          #
# CSE                                #
#                                    #
######################################

from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    # return "Welcome to my web api"
    # return "Welcome to my web api"
    return '<h1>Hello, Uddin!</h1>'
@app.route('/something',methods=['GET'])
def onno_kichu():
    return "mathai ki r kichu nai"

if __name__ == '__main__':
    app.run()
