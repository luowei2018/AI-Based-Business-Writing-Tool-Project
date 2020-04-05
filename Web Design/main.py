from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("first.html")
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/check")
def check():
    return render_template("check.html")

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)

