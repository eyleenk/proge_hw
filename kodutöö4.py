import mysql.connector
import hashlib

mydb = mysql.connector.connect(
		host="sql11.freemysqlhosting.net",
		user="sql11704711",
		password="7WspYXGQ8s",
		database="sql11704711"
	)
mycursor = mydb.cursor()

def create_table():
	global mycursor
	mycursor.execute("CREATE TABLE IF NOT EXISTS usercredentials(id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) NOT NULL, password VARCHAR(255))")

def create_account(user: str, password: str):
	global mycursor, mydb
	hashed = hashlib.sha256(password.encode()).hexdigest()
	mycursor.execute("SELECT * FROM usercredentials WHERE username = '" + user + "'")
	if len(mycursor.fetchall()) < 1:
		mycursor.execute("INSERT INTO usercredentials(username, password) VALUES (%s, %s)", (user, hashed))
		mydb.commit()
	else:
		print("user already exists")

def login(user: str, password: str):
	global mycursor
	hashed = hashlib.sha256(password.encode()).hexdigest()
	mycursor.execute("SELECT * FROM usercredentials WHERE username = %s AND password = %s", (user, hashed))
	mycursor.fetchall()
	if mycursor.rowcount == 1:
		print("login successful")
	else:
		print("login failed")

def menu():                                
    print("=" * 25)                        
    print("Please Select An Option")
    print("=" * 25)
    print("")
    print("1. create account\n")
    print("2. login\n")
    print("3. close database connection\n")
    menuOption = int(input("Select Option: "))
    if menuOption == 1:
        username = input("username: ")
        password = input("password: ")
        create_account(username, password)
        menu()
    elif menuOption == 2:
        username = input("username: ")
        password = input("password: ")
        login(username, password)
        menu()
    elif menuOption == 3:
        global mydb
        mydb.close()
    else:
        print("Invalid option")
        menu()

def main():
	create_table()
	menu()

main()
