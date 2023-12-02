"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

file_path_customer = 'north_data/customers_data.csv'
file_path_order = 'north_data/orders_data.csv'
file_path_employees = 'north_data/employees_data.csv'

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='1379')

try:
    with conn:
        with conn.cursor() as cur:
            with open(file_path_customer, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                cur.executemany(
                    'INSERT INTO customers (customer_id, company_name, contact_name)'
                    'VALUES (%s, %s, %s)',
                    reader
                )

            with open(file_path_employees, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                cur.executemany(
                    'INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes)'
                    'VALUES (%s, %s, %s, %s, %s, %s)',
                    reader
                )

            with open(file_path_order, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                cur.executemany(
                    'INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city)'
                    'VALUES (%s, %s, %s, %s, %s)',
                    reader
                )

        conn.commit()

finally:
    conn.close()
