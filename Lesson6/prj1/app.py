from flask import Flask, render_template, request

app = Flask(__name__)

def convert_units(value, from_unit, to_unit):
    conversion_factors = {
    'cm': {'m': 0.01, 'km': 0.00001, 'inch': 0.393701, 'foot': 0.0328084},
    'm': {'cm': 100, 'km': 0.001, 'inch': 39.3701, 'foot': 3.28084},
    'km': {'cm': 100000, 'm': 1000, 'inch': 39370.1, 'foot': 3280.84},
    'inch': {'cm': 2.54, 'm': 0.0254, 'km': 0.0000254, 'foot': 0.0833333},
    'foot': {'cm': 30.48, 'm': 0.3048, 'km': 0.0003048, 'inch': 12}
    }
    if from_unit == to_unit:
        return value
    return value * conversion_factors.get(from_unit, {}).get(to_unit, 1)

@app.get("/")
def main():
    return render_template("tst_index.html")

@app.post("/")
def convert():
    try:
        value = float(request.form.get("value"))
        from_unit = request.form.get("from_unit")
        to_unit = request.form.get("to_unit")
        result = convert_units(value, from_unit, to_unit)
    except ValueError:
        result = "Помилка: введи число"
    return render_template("tst_index.html", result=result)



if __name__ == '__main__':
    app.run(debug=True, port=5033)