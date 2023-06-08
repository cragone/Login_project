from flask import Flask, render_template, request
from functions.accounts import storeuserdata

app = Flask(__name__)

@app.route("/login_page")
def index():
    return render_template("login_page.html")

@app.route('/sign_in')
def sign_in():
    un = request.args.get('username',None,str)
    return 'Hey there %s' % un  

@app.route("/info", methods=['POST'])
def information():
    username = request.args.get("token",None,str)

@app.route('/register', methods=['GET'])
def reg_page():
    return render_template("register.html")

@app.route('/registeruser', methods=['POST', 'GET'])
def post_userdata():
    username = request.args.get("username",None,str)
    password = request.args.get("password",None,str)
    email = request.args.get("email",None,str)
    print(username, password, email)
    return storeuserdata(username, password, email)
      
    
    



if __name__ == '__main__':
    app.run(debug=True)
