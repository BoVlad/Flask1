from flask import Flask, render_template


app = Flask(__name__)



@app.get('/')
def index():
    return render_template("inde.html")

@app.get('/contact/')
def contact():
    return render_template("contact.html")

@app.get('/about/')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True, port=5001)