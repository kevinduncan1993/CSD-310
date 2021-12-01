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

    print("-- Displaying players after delete --")
    
    cursor = db.cursor()
    query = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id "
    cursor.execute(query)
    rows = cursor.fetchall()
    for x in rows:
        print("Player ID: {} ".format(x[0]))
        print("First Name: {} ".format(x[1]))
        print("Last Name: {} ".format(x[2]))
        print("Team Name: {} ".format(x[3]))
        print("")

        


    db.close()

    print("\n Database user{} connected to MYSQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    
    
   
    

    cursor = db.cursor()
    cursor.execute("SELECT player_id, first_name,  last_name , team_id FROM player") 
    players = cursor.fetchall()
    print("-- DIsplaying Player Record --")
    for player in players:
        print("Player ID: {} ".format(player[0]))
        print("First Name: {} ".format(player[1]))
        print("Last Name: {} ".format(player[2]))
        print("Team _ID: {} ".format(player[3]))
        print("")
       

    #update record for Tyrod Taylor to Desmond Ridder
    cursor = db.cursor()
    query = "UPDATE player SET team_id = '229', first_name = 'Desmond', last_name = 'Ridder' WHERE first_name = 'Tyrod'"
    cursor.execute(query)
    db.commit()
    
    
    
    #Inserted new data into table
    #mySql_insert_data =  """INSERT INTO player (first_name, last_name, team_id, player_id)
    #VALUES("Tyrod", "Taylor", "229", 21)"""
    #cursor = db.cursor()
   # cursor.execute(mySql_insert_data)
    #db.commit()
    #db.close()
      
    
    #Delets query from updated record
    cursor = db.cursor()
    sql_delete_query = "DELETE FROM player WHERE first_name = 'Desmond' "
    cursor.execute(sql_delete_query)
    db.commit()
    db.close()



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
 