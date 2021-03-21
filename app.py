from flask import(
    Flask, render_template,request,session,redirect,url_for)


class User:
    def __init__(self,id,username,password):
        self.id=id
        self.username= username
        self.password= password
    def __repr__(self):
        return f'<User:{self.username}'

users=[]
users.append(User(id=1,username='Darek',password='password'))

print(users)
app = Flask(__name__)
app.secret_key='sekretnyklucz'
@app.route('/', methods=('GET','POST'))
def login():
    if request.method =='POST':
        session.pop('user_id',None)
        username=request.form['username']
        password=request.form['password']

        user=[x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id']=user.id
            return redirect(url_for('calculator'))

        return redirect(url_for('login'))

    return render_template('login.html')

@app.route("/calculator" ,methods=('GET','POST'))
def calculator():
    return render_template('calculator.html')

@app.route('/example', methods=('GET','POST'))
def example():
    lhs=float(request.form['firstnumber'])
    rhs=float(request.form['secondnumber'])
    op=request.form['sing']
    result=0
    if(lhs==0 or rhs==0 and op=="/"):
        result=0
    else:
        if(op=="+"):
            result=lhs+rhs
        elif(op=="-"):
            result=lhs-rhs
        elif(op=="*"):
            result=lhs*rhs
        elif(op=="/"):
            result=lhs/rhs

    return str(result)


if __name__=='__main__':
    app.run(debug=True)