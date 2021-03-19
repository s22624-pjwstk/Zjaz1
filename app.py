from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/')
def mian():
    return render_template('index.html')

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
