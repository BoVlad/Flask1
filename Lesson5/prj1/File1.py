from flask import Flask, render_template, request
import random as r
from datetime import datetime

app = Flask(__name__)

list1 = ["Сьогодні у вас", "Завтра на вас", "Незабаром"]
list2 = ["чекає", "буде", "зустріне"]
list3 = ["гарна новина", "погана звіска", "гарний день", "поганий день"]
books = ["Harry Potter", "Лабіринт", "Пайтон для новачків"]
fruits_list = [{"name": "Яблуко", "color": "red"},
               {"name": "Банан", "color": "yellow"},
               {"name": "Груша", "color": "green"},
               {"name": "Вишня", "color": "red"},
               {"name": "Ківі", "color": "green"},
               {"name": "Апельсин", "color": "orange"}]

@app.get('/')
def hello_world():
    name = request.args.get("name")
    age = request.args.get("age")
    if name is None:
        name = "Anonim"
    if age is None:
        age = 1
    return render_template("inde.html", name=name, age=int(age))

@app.post("/")
def add_fruits():
    action = request.form.get("action")
    name = request.form.get("name")
    color = request.form.get("color")
    if action == "add_fruit":
        fruits_list.append({"name": name, "color": color})
    if action == "delete_fruit": #Я наверное что то не так в рендер темплейтах написал, не в том порядке | не работает микрофон
        for i in fruits_list:
            if i.get("name") == name:
                fruits_list.remove(i)
    return render_template("recipec.html", fruits=fruits_list)

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


@app.get("/books/")
def get_books():
    return render_template("books.html", books=books)





if __name__ == '__main__':
    app.run(debug=True, port=5002)