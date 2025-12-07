from flask import Flask, render_template, request
import random as r
from datetime import datetime

app = Flask(__name__)

list1 = ["Сьогодні", "Завтра", "Скоро", "Потужно", "Незабаром"]
list2 = ["на вас", "на тебе", "тебе", "вас"]
list3 = ["чекає", "може напасти", "зустріне", "попотужнічає", "заохоче"]
list4 = ["гарна новина", "погана звістка", "потужність", "непотужність", "гарний день", "поганий день", "23 кредити", "лужа"]
list5 = ["а також", "але", "а ще", "без росслаблення", "і можливо"]
list6 = ["!", ".", ")"]

@app.get('/')
def hello_world():
    name = "Vlad"
    return render_template("inde.html", name=name, hobby=datetime.now())

@app.get("/data/")
def data():
    return render_template("greet.html")

@app.get('/submit/')
def post_submit():
    name = request.form['name']
    return f"Привіт, {name}!"


@app.post('/submit/')
def post_submit():
    name = request.form['name']
    return f"Привіт, {name}!"

@app.get('/horoskop/')
def horoskop():
    return f"{r.choice(list1)} {r.choice(list2)} {r.choice(list3)} {r.choice(list4)}, {r.choice(list5)}, {r.choice(list4)}{r.choice(list6)}"

if __name__ == '__main__':
    app.run(debug=True, port=5001)