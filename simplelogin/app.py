from flask import Flask, render_template

app = Flask(__name__)

@app.route("/login_page")
def index():
    return render_template("login_page.html")


if __name__ == '__main__':
    app.run(debug=True)
