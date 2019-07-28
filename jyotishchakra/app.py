from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/aboutus")
def aboutus():
    return render_template("about.html")

@app.route("/contactus")
def contactus():
    return render_template("contact.html")

@app.route("/horoscope")
def horoscope():
    return render_template("horoscope.html")

@app.route("/numerology")
def numerology():
    return render_template("numerology.html")

@app.route("/tarot")
def tarot():
    return render_template("tarot.html")

@app.route("/vastu")
def vastu():
    return render_template("vastu.html")

@app.route("/palm")
def palm():
    return render_template("home.html")

@app.route("/reiki")
def reiki():
    return render_template("reiki.html")

@app.route("/theta")
def theta():
    return render_template("theta.html")

if __name__=='__main__':
     app.run(host='0.0.0.0',debug=True)

