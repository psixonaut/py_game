import sqlite3


def get_all_names():
    # возврат всех имен из бд
    con = sqlite3.connect("pl_prj.sqlite")
    cur = con.cursor()
    need1 = """SELECT name FROM plants"""
    names = cur.execute(need1).fetchall()
    cur.close()
    con.close()
    return names


def delete_item(name, speciality, regularity):
    # удаление строки из бд
    con = sqlite3.connect("pl_prj.sqlite")
    cur = con.cursor()
    cur.execute(f"DELETE FROM plants WHERE name='{name}' AND speciality='{speciality}'"
                f" AND regularity='{regularity}'")
    con.commit()
    cur.close()
    con.close()


def get_all():
    # выбор всех элементов бд
    con = sqlite3.connect("pl_prj.sqlite")
    cur = con.cursor()

    need = """SELECT * FROM plants"""

    plants = cur.execute(need).fetchall()
    return plants


def update_item(new_name, new_speciality, new_regularity, name, speciality, regularity):
    # сохранение измененной ячейки в бд
    con = sqlite3.connect("pl_prj.sqlite")
    cur = con.cursor()

    cur.execute(f"UPDATE plants SET name='{new_name}', speciality='{new_speciality}', "
                   f"regularity='{new_regularity}'"
                   f" WHERE name='{name}' AND speciality='{speciality}' AND regularity='{regularity}'")

    con.commit()
    cur.close()
    con.close()

