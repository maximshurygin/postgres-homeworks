-- SQL-команды для создания таблиц

CREATE TABLE employees
(
	employee_id serial PRIMARY KEY,
	first_name varchar(20) NOT NULL,
	last_name varchar(20) NOT NULL,
	title varchar(50) NOT NULL,
	birth_date DATE NOT NULL,
	notes text)


CREATE TABLE customers
(
	customer_id char(5) NOT NULL,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL
)

CREATE TABLE orders
(
	order_id serial PRIMARY KEY,
	customer_id char(5) NOT NULL,
	employee_id serial,
	order_date DATE NOT NULL,
	ship_city varchar(20) NOT NULL
)