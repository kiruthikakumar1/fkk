from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)


@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/hello')
def helloworld():
    return render_template('hello.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    err=None
    if request.method=='POST':
        if request.form['uname']!='kiruthi' or request.form['passwd']!='123':
            err='Invalid username and password!!!'
        else:
            return redirect(url_for('home'))
    return render_template('login.html',err=err)


if __name__=='__main__':
    app.run()