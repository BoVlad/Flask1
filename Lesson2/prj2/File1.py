from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def hello_world():
    name = "Влад"
    age = 14
    hobby = "Програмування"
    place_to_visit = "Не знаю"
    return render_template("inde.html", name=name, age=age, hobby=hobby, place_to_visit=place_to_visit)

if __name__ == '__main__':
    app.run(debug=True, port=5001)