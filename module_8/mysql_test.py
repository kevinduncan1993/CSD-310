import mysql.connector
from mysql.connector import errorcode


db = mysql.connector.connect()
db.close()

config = {
    'user':"test_user",
    'password':'kevin28',
    'host': '127.0.0.1',
    'database':'pytest',
    'raise_on_warnings': True
}


try:
    #db = mysql.connector.connect (**config)
    print("\n Database user{} connected to MYSQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...") 

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_CHANGE_USER_ERROR:
        print("\n\n The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("The specified database does not exist")

    else:
        print(err)

finally:
 db.close()
