from flask import Flask, render_template, request

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
    username = request.arg.get("token",None,str)

@app.route('/register')
def reg_page():
    return render_template("register.html")

# @app.route('/resgistered', methods=['POST'])
# def post_request():
#       content = request.args.get("Username", None, str)
#     if content is None:
#         return "Server Error", 400
#     connection = psycopg2.connect(
#                     user="postgres",
#                     password="postgrespostgres",
#                     host="localhost",
#                     port="5432",
#                     database="loginbase"
#              )
#     cursor = connection.cursor()

#     insert_query = "INSERT INTO tweets (content) VALUES (%s); COMMIT;"
#     cursor.execute(insert_query, (content,))
    
    



if __name__ == '__main__':
    app.run(debug=True)
