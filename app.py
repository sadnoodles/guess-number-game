#encoding:utf-8
# git@heroku.com:pytest1091.git
import os,time
from flask import Flask,request
from flask import render_template
# import md5
app = Flask(__name__)
import guessNumber as GN
    
@app.route('/', methods=['GET', 'POST'])
def guessNumber():
    # print request.form
    # print 
    # print request.values
    GN.getWebInput=lambda :request.form['getText']
    # GN.getWebInput=lambda :"1234"
    if request.method == 'POST':
        if GN.gameOver():
            GN.newGame()
        GN.oneGuess()
    else:
        GN.newGame()
    return render_template('guess.html',history=GN.history)
    
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    
    port = int(os.environ.get('PORT',0))
    if port:
        app.run(host='0.0.0.0', port=port)
    else:
        app.run(host='0.0.0.0', port=5000,debug=True,threaded=True)
