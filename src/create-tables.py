import sqlite3


if __name__ == "__main__":

    connection = sqlite3.connect('events.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS CUSTOMER (type text, verb text, key text, event_time text, last_name text, adr_city text,adr_state text)')
    cursor.execute('CREATE TABLE IF NOT EXISTS VISIT (type text, verb text, key text, event_time text, customer_id text, tags text)')
    cursor.execute('CREATE TABLE IF NOT EXISTS IMAGE (type text, verb text, key text, event_time text, customer_id text,camera_make text,camera_model text)')
    cursor.execute('CREATE TABLE IF NOT EXISTS ORDERS (type text, verb text, key text, event_time text, customer_id text, total_amount text)')

    connection.commit()
    connection.close()

