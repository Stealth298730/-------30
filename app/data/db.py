import sqlite3
def get_pizzas1() -> list:
    data = []
    try:
        sql_con = sqlite3.connect("pizzas1.db")
        cursor = sql_con.cursor()

        query = "SELECT * FROM pizzas1"

        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        print("Дані успішно записані")

    except sqlite3.Error as error:
        print(f"{error = }")

    finally:
        if sql_con:
            sql_con.close()
            print("Робота з базою даних успішно завершена")
        return data


def create_table():
    try:
        sql_con = sqlite3.connect("pizzas1.db")
        cursor = sql_con.cursor()


        with open("create_db.sql", "r") as file:
            query = file.read()

        cursor.execute(query)
        sql_con.commit()
        cursor.close()
        print("Таблиця успішно створена")

    except sqlite3.Error as error:
        print(f"Помилка: {error}")

    finally:
        if sql_con:
            sql_con.close()
            print("З'єднання з базою даних закрито")


def insert_data(
    first_name: str,
    price: int | None = None,
    ingredients: str | None = None,
) -> None:
    try:
        sql_con = sqlite3.connect("pizzas1.db")
        cursor = sql_con.cursor()


        query = "INSERT INTO pizzas1 (first_name, price, ingredients) VALUES (?, ?, ?)"
        data = (first_name, price, ingredients)

        cursor.execute(query, data)
        sql_con.commit()
        cursor.close()
        print("Дані успішно записані")

    except sqlite3.Error as error:
        print(f"Помилка: {error}")

    finally:
        if sql_con:
            sql_con.close()
            print("З'єднання з базою даних закрито")
