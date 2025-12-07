from flask import Flask, render_template, request
import random as r
from datetime import datetime

app = Flask(__name__)

list1 = ["Сьогодні у вас", "Завтра на вас", "Незабаром"]
list2 = ["чекає", "буде", "зустріне"]
list3 = ["гарна новина", "погана звіска", "гарний день", "поганий день"]


@app.get('/')
def hello_world():
    name = "Kostya"
    return render_template("inde.html", name=name,
                           hobby=datetime.now
                           ())

@app.get("/data/")
def data():
    data = request.args.get("info")
    data2 = request.args.get("info2")
    if data != None:
        return f"Ваша інформація: {data} {data2}"
    return f"Немає інформації"


@app.get('/submit/')
def get_submit():
    return render_template("submit.html")


@app.post('/submit/')
def post_submit():
    name = request.form['name']
    return f"Привіт, {name}!"


@app.get("/horoskop/")
def horoskop():
    return f"{r.choice(list1)} {r.choice(list2)} {r.choice(list3)}"


if __name__ == '__main__':
    app.run(debug=True, port=5002)