from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods = ["GET","POST"])
def submit():
    if request.method == "POST":
        return redirect(url_for("page"))

@app.route("/page")    
def page():
    return render_template("page.html")


if __name__ == "__main__":
    app.run(debug=True)