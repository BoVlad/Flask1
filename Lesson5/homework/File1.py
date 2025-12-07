from flask import Flask, render_template, request

app = Flask(__name__)


recipes_list = [
    {"name": "Вівсянка з фруктами", "type": "сніданок", "difficulty": "легка"},
    {"name": "Яєчня з овочами", "type": "сніданок", "difficulty": "середня"},
    {"name": "Борщ український", "type": "обід", "difficulty": "складна"},
    {"name": "Паста з куркою", "type": "обід", "difficulty": "середня"},
    {"name": "Салат Цезар", "type": "обід", "difficulty": "легка"},
    {"name": "Запечена риба з овочами", "type": "вечеря", "difficulty": "середня"},
    {"name": "Тушковані овочі", "type": "вечеря", "difficulty": "легка"},
    {"name": "Стейк з картоплею", "type": "вечеря", "difficulty": "складна"},
]
@app.get("/")
def index():
    return render_template("index.html")

@app.post("/result")
def result():
    types = request.form.get("type")
    difficulty = request.form.get("difficulty")

    filtereded = []
    for i in recipes_list:
        if i["type"] == types and i["difficulty"] == difficulty:
            filtereded.append(i)
    return render_template("recipec.html", recipes=filtereded)

if __name__ == "__main__":
    app.run(debug=True, port=5002)