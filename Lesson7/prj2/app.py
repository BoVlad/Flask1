from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

info_db = []
@app.get("/register")
def register_g():
    return render_template("register.html")

@app.post("/register")
def register_p():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    info_db.append({"name": name, "email": email, "password": password})
    return redirect(url_for("login_g"))
@app.get("/login")
def login_g():
    return render_template("login.html")

@app.post("/login")
def login_p():
    name = request.form.get("name")
    password = request.form.get("password")
    for i in info_db:
        if i["name"] == name and i["password"] == password:
            return "Вхід успішно виконано!"
    return "Вхід не виконано!"


if __name__ == "__main__":
    app.run(debug=True, port=5002)