'''John Hadden,Kevin Finnissee, Jonathan Kobyluck
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
    print("--- This report generates how many transactions a client has made in a month  --- ")
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    query = "SELECT clients.client_id, clients.client_first_name, clients.client_last_name, transactions.transaction_id, transactions.day, transactions.month FROM clients INNER JOIN transactions ON clients.client_id = transactions.client_id" 
    cursor.execute(query)
    rows = cursor.fetchall()
    
    
    for x in rows:
        print("Client ID: {} ".format(x[0]))
        print("Client First Name: {} ".format(x[1]))
        print("Client Last Name: {} ".format(x[2]))
        print("Transaction ID: {} ".format(x[3]))
        print("Day: {} ".format(x[4]))
        print("Month: {} ".format(x[5]))
        print("")
    db.close()

    
        
   




    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))





    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)