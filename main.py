from flask import Flask, render_template, request, redirect

from app.data import db


app = Flask(__name__, static_folder="app/static", template_folder="app/templates")


@app.get("/")
def index():
    return render_template("index.html", title="Головна сторінка")


@app.get("/pizzas/")
def show_pizzas():
    pizzas = db.get_pizzas1()
    context = {
        "title": "Список піц",
        "pizzas": pizzas
    }
    return render_template("pizzas.html", **context)


@app.get("/add_pizza/")
def add_pizza():
    return render_template("add_pizza.html", title="Додати нову піццу")


@app.post("/add_pizza/")
def add_pizza_post():
    data = request.form
    print(f"{data = }")
    db.insert_data(**data)
    return redirect("/pizzas/", code=302)


if __name__ == "__main__":
   app.run(debug=True)
