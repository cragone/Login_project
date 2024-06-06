from flask import Flask, render_template, request
from flask_mail import Mail, Message
from functions.accounts import storeuserdata, retrieve_hashed_password
import hashlib

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'runclubhousesllc@gmail.com'
app.config['MAIL_PASSWORD'] = 'wqmccxdqxegmutba'
app.config['MAIL_DEFAULT_SENDER'] = 'runclubhousesllc@gmail.com'
mail = Mail(app)


@app.route('/sign_in', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        stored_hashed_password = retrieve_hashed_password(username)
        hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        if stored_hashed_password == hashed_password:
            return render_template("home_page.html") 
        else:
            return 'Invalid username or password'
    else:
        return 'Invalid request method'



@app.route('/registeruser', methods=['POST', 'GET'])
def post_userdata():
    username = request.args.get("username",None,str)
    password = request.args.get("password",None,str)
    email = request.args.get("email",None,str)
    hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
    
    print(username, hashed_password, email)
    return storeuserdata(username, hashed_password, email)
    


@app.route('/send_email', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        email = request.form.get('email')  
        msg = Message("Verify HERE", sender='noreply@runclub.com', recipients=[email])
        msg.body = "Welcome to RUNCLUB, please verify your email here"
        mail.send(msg)
        return "Email sent successfully."
    else:
        return "Invalid request."


    



if __name__ == '__main__':
    app.run(debug=True)
