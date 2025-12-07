from flask import Flask, render_template, request, session, render_template_string, make_response
import requests

app = Flask(__name__)
app.secret_key = "AprioriKS"

PHP_API_URL = "https: // justconsole.tech / python / api.php?table = users"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="uk">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Паролі користувачів</title>

</head>
<body>

<h1>Паролі користувачів</h1>
{% for user in users %}

<p><strong>ім'я користувача:</strong> {{ user.username }} | <strong>пароль:</strong> {{ user.password

}}</p>
{% endfor %}

</body>
</html>
"""

adad
@app.get("/")
def home():
    user_agent = request.headers.get("User-Agent")
    name = request.cookies.get("username")
    if "clicks" not in session:
        session["clicks"] = 0
    return render_template_string("""`
    <h1>{{name}}</h1>
    <h1>{{user_agent}}</h1>
    <h1>Кількість кліків: {{ clicks }}</h1>
    <a href="/click">Натисни!</a>
    `""", clicks=session["clicks"], name=name, user_agent=user_agent)


@app.get("/click")
def click():
    session["clicks"] += 1
    return home()


@app.get("/cookies/")
def set_cookies():
    res = make_response("Setings coockie")
    res.set_cookie("username", "Kostya", max_age=60 * 60 * 24 * 365 * 2)
    return res


@app.get("/example/<int:id>/")
def example(id):
    return f"Отримано число: {id + id}"


@app.get("/example/<string:text>/")
def text(text):
    return f"Отримано текст: {text}"


@app.get("/users/")
def get_users():
    try:
        response = requests.get(PHP_API_URL)
        users = response.json()  # Отримуємо список користувачів
        return render_template_string(HTML_TEMPLATE, users=users)

    except requests.exceptions.RequestException as e:
        return f"<p>Помилка при підключенні до сервера: {str(e)}</p>"


if __name__ == '__main__':
    app.run(debug=True, port=5004)