'''John Hadden
12/2/2021
Module 10 Assignment 10.3
Create tables and values with Python Script for Database within MySQL'''

import mysql.connector
from mysql.connector import errorcode


db = mysql.connector.connect()
db.close()

config = {
    "user": "pysports_root",
    "password": "Finnissee1!",
    "host": "127.0.0.1",
    "database": "Willsonf",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

    cursor = db.cursor()

    cursor.execute('''
    CREATE TABLE clients (
        client_id           INT           NOT NULL,
        client_first_name   VARCHAR(300)   NOT NULL,
        client_last_name    VARCHAR(300)   NOT NULL,
        start_day           INT           NOT NULL,
        start_month         VARCHAR(300)   NOT NULL,
        start_year          INT           NOT NULL,
        beginning_assets    INT           NOT NULL,
        current_assets      INT           NOT NULL,
        PRIMARY KEY(client_id)
        );

    INSERT INTO clients(client_id, client_first_name, client_last_name, start_day, start_month, start_year, beginning_assets, current_assets)
        VALUES('10345', 'Joseph', 'Harrison', '05', 'SEPTEMBER', '2010', '100',   '3796'),
              ('11571', 'Megan',  'Robinson', '29', 'SEPTEMBER', '2011', '10000', '59008'),
              ('10918', 'Thomas', 'Peters',   '01', 'JANUARY',   '2017', '26000', '40100'),
              ('17661', 'David',  'Morgan',   '11', 'SEPTEMBER', '2020', '100',   '9900'),
              ('11672', 'Emily',  'Stetson',  '01', 'SEPTEMBER', '2020', '100',   '6100'),
              ('19012', 'Harold', 'Smith',    '21', 'APRIL',     '2020', '5000',  '7510');

    CREATE TABLE employees (
        employee_id        INT            NOT NULL,
        emp_first_name         VARCHAR(300)    NOT NULL,
        emp_last_name          VARCHAR(300)    NOT NULL,
        department_name    VARCHAR(300)    NOT NULL,
        department_id      INT            NOT NULL,
        PRIMARY KEY(employee_id)
        );

    INSERT INTO employees(employee_id, emp_first_name, emp_last_name, department_name, department_id)
        VALUES('0001', 'Jake',    'Willson',  'EXECUTIVE',  '01'),
              ('0002', 'Ned',     'Willson',  'EXECUTIVE',  '01'),
              ('0003', 'Pheonix', 'Two Star', 'OFFICE',     '02'),
              ('0004', 'June',    'Santos',   'COMPLIANCE', '03');

    CREATE TABLE transactions (
        transaction_id      INT           NOT NULL,
        day                 INT           NOT NULL,
        month               VARCHAR(300)  NOT NULL,
        year                INT           NOT NULL,
        client_id           INT           NOT NULL,
        amount              INT           NOT NULL,
        PRIMARY KEY(transaction_id)
        );

    INSERT INTO transactions(transaction_id, day, month, year, client_id, amount)
        VALUES('574899', '05', 'SEPTEMBER', '2010', '10345', '100'),
              ('012715', '29', 'SEPTEMBER', '2011', '11571', '1000'),
              ('991021', '01', 'JANUARY', '2017', '10918', '26000'),
              ('411126', '11', 'SEPTEMBER', '2020', '17661', '100'),
              ('999161', '01', 'SEPTEMBER', '2020', '11672', '100'),
              ('001672', '21', 'APRIL', '2020', '19012', '5000'),
              ('501012', '06', 'JANUARY', '2013', '10345', '1000'),
              ('818789', '06', 'FEBRUARY', '2014', '11571', '20000'),
              ('112140', '06', 'JUNE', '2018', '10918', '20000'),
              ('124617', '06', 'JULY', '2020', '19012', '1000');

    ''')
