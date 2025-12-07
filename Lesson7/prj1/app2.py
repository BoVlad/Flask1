from flask import Flask, render_template_string, request, redirect, session
import requests
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# URL API для зберігання даних користувачів
PHP_API_URL = "https://justconsole.tech/python/api.php?table=users_new"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="uk">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Реєстрація</title>

</head>
<body>

<h1>список користувачів</h1>
{% for user in users %}
    <p><strong>ім'я:</strong> {{ user.username }} | 
       <strong>email:</strong> {{ user.email }} | 
       <strong>пароль (хеш):</strong> {{ user.password }}</p>
{% endfor %}

<h2>форма для нових користувачів</h2>
<form method="POST" action="/register">
    <input type="text" name="username" placeholder="ім'я користувача" required>
    <input type="email" name="email" placeholder="email" required>
    <input type="password" name="password" placeholder="пароль" required>
    <button type="submit">створити користувача</button>
</form>

<h2>форма для входу</h2>
<form method="POST" action="/login">
    <input type="text" name="username" placeholder="ім'я користувача" required>
    <input type="password" name="password" placeholder="пароль" required>
    <button type="submit">увійти</button>
</form>

</body>
</html>
"""

@app.get("/")
def home():
    # Отримуємо список користувачів з API
    try:
        response = requests.get(PHP_API_URL)
        response.raise_for_status()
        users = response.json()
        return render_template_string(HTML_TEMPLATE, users=users)
    except requests.exceptions.RequestException as e:
        return f"<p>халепа з апі: {str(e)}</p>"


@app.post("/register")
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    data = {

        "username": username,
        "email": email,
        "password": password  # Зберігаємо пароль у відкритому вигляді

    }

    try:
        response = requests.post(PHP_API_URL, json=data)
        if response.status_code == 200:
            return redirect("/")
        else:
            return f"<p>халепа: {response.text}</p>"
    except requests.exceptions.RequestException as e:
        return f"<p>халепа з апі: {str(e)}</p>"


@app.post("/login")
def login():

    username = request.form['username']
    password = request.form['password']

    try:
        # Отримуємо список користувачів з API
        response = requests.get(PHP_API_URL)
        users = response.json()

        # Знаходимо користувача в базі
        user = next((user for user in users if user['username'] == username), None)

        if user:
            print(f"Знайдений користувач: {user['username']}, Пароль: {user['password']}") # Діагностика
            # Хешуємо введений пароль з 10 раундами
            hashed_input_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=10))

            # Перевірка пароля
            if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')): # Порівнюємо збережений хеш з введеним паролем
                # Якщо користувача знайшли і пароль збігається
                session['user'] = user['username'] # Зберігаємо ім'я користувача в сесії
                return f"<h1>Ласкаво просимо, {user['username']}!</h1>"

            else:
                return "<p>Невірний пароль!</p>"
        else:
            return "<p>Невірний логін!</p>"
    except requests.exceptions.RequestException as e:
        return f"<p>Помилка при перевірці: {str(e)}</p>"


if __name__ == '__main__':
    app.run(debug=True, port=5002)



