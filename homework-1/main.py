"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="2142"
)

try:
    with open('north_data/employees_data.csv') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        employees_data = [tuple(row) for row in csv_reader]

    with conn:
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", employees_data)

    with open('north_data/customers_data.csv') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        customer_data = [tuple(row) for row in csv_reader]

    with conn:
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", customer_data)

    with open('north_data/orders_data.csv') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        orders_data = [tuple(row) for row in csv_reader]

    with conn:
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", orders_data)

finally:
    conn.close()
