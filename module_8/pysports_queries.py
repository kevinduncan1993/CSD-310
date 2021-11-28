import mysql.connector
from mysql.connector import errorcode


db = mysql.connector.connect()
db.close()

config = {
    'user':"pysports_root",
    'password':'Finnissee1!',
    'host': '127.0.0.1',
    'database':'pysports',
    'raise_on_warnings': True
}



try:
    db = mysql.connector.connect (**config)
    print("\n Database user{} connected to MYSQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    cursor = db.cursor()
    cursor.execute("SELECT team_id, team_name,  mascot FROM team")
    teams = cursor.fetchall()
    print("-- Displaying Team Records --")
    for team in teams:
     
        print("Team ID: {} ". format(team[0]))
        print("Team name: {} ". format(team[1]))
        print("Mascot: {} ". format(team[2]))
        print("")
   
    cursor.execute("SELECT player_id, first_name,  last_name , team_id FROM player") 
    players = cursor.fetchall()
    print("-- DIsplaying Player Record --")
    for player in players:
        print("Player ID: {} ".format(player[0]))
        print("First Name: {} ".format(player[1]))
        print("Last Name: {} ".format(player[2]))
        print("Team ID: {} ".format(player[3]))
        print("")

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
