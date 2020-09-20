import psycopg2


def create():
    conn = psycopg2.connect("dbname='postgres' host='localhost' port='5432' user='postgres' password='04111987A'")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT , quantity INTEGER ,price REAL)")
    conn.commit()
    cursor.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='postgres' host='localhost' port='5432' user='postgres' password='04111987A'")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()
    cursor.close()


def view():
    conn = psycopg2.connect("dbname='postgres' host='localhost' port='5432' user='postgres' password='04111987A'")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    conn.commit()
    cursor.close()
    return rows


def update(quantity, price, item):
    conn = psycopg2.connect("dbname='postgres' host='localhost' port='5432' user='postgres' password='04111987A'")
    cursor = conn.cursor()
    cursor.execute("UPDATE store SET quantity = %s,price = %s WHERE item = %s", (quantity, price, item))
    conn.commit()
    cursor.close()


def delete(item):
    conn = psycopg2.connect("dbname='postgres' host='localhost' port='5432' user='postgres' password='04111987A'")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM store WHERE item = %s", (item,))
    conn.commit()
    cursor.close()


create()
# insert("CDDCC", 10, 2.3)

# update(143, 115.2, 'CDDCC')
delete('BBB')
print(view())
