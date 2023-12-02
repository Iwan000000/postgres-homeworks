-- SQL-команды для создания таблиц

CREATE TABLE employees
(
    employee_id int PRIMARY KEY,
 	first_name varchar(100),
	last_name varchar(100),
	title varchar(100),
 	birth_date date,
	notes text
);

CREATE TABLE customers (
    customer_id text PRIMARY KEY,
    company_name VARCHAR(100),
    contact_name VARCHAR(100)
);
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id text REFERENCES customers (customer_id),
    employee_id INT REFERENCES employees (employee_id),
    order_date DATE,
    ship_city varchar(100)
);
