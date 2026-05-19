from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/member1')
def member1():
    return render_template('member1.html')

@app.route('/member2')
def member2():
    return render_template('member2.html')

@app.route('/member3')
def member3():
    return render_template('member3.html')

@app.route('/member4')
def member4():
    return render_template('member4.html')

@app.route('/member5')
def member5():
    return render_template('member5.html')

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
