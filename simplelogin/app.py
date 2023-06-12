from flask import Flask, render_template, request
from flask_mail import Mail, Message
from functions.accounts import storeuserdata

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'runclubhousesllc@gmail.com'
app.config['MAIL_PASSWORD'] = 'wqmccxdqxegmutba'
app.config['MAIL_DEFAULT_SENDER'] = 'runclubhousesllc@gmail.com'
mail = Mail(app)

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

@app.route('/send_email', methods=['GET','POST'])
def send_email():
      if request.method == 'POST':
          msg = Message("Verify HERE", sender='noreply@runclub.com', recipients=['email'])
          msg.body = "Welcome to RUNCLUB, please verify email here"
          mail.send(msg)
          return "sent email."  

    



if __name__ == '__main__':
    app.run(debug=True)
