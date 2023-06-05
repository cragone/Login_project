from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/login_page")
def index():
    return render_template("login_page.html")

@app.route('/sign_in')
def sign_in():
    un = request.args.get('username',None,str)
    return 'Hey there %s' % un  


if __name__ == '__main__':
    app.run(debug=True)
