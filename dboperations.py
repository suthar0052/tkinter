import sqlite3


def create():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT , quantity INTEGER ,price REAL)")
    conn.commit()
    cursor.close()


def insert(item, quantity, price):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    cursor.close()


def view():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    conn.commit()
    cursor.close()
    return rows


def update(quantity, price, item):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE store SET quantity = ?,price=? WHERE item = ?", (quantity, price, item))
    conn.commit()
    cursor.close()


def delete(item):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM store WHERE item = ?", (item,))
    conn.commit()
    cursor.close()


create()
# insert("BBB", 10, 2.3)
update(14, 15.2, 'AAA')
delete('BBB')
print(view())
