from flask import Flask, render_template, request

app = Flask(__name__)

@app.get('/')
def hello_world():
    return render_template("inde.html")


@app.post('/submit/')
def post_submit():
    name = request.form['name']
    age = request.form['age']
    color = request.form['color']
    return render_template("greet.html", name=name, age=age, color=color)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

    