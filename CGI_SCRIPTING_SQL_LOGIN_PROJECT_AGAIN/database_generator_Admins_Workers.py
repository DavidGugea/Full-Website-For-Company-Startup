import sqlite3, sys, random

database = sqlite3.connect("PythonDatabase.db")
database_cursor = database.cursor()

database_cursor.execute("CREATE TABLE IF NOT EXISTS admins_workers(first_name TEXT, second_name TEXT, age INTEGER, city TEXT, post_code INTEGER, salary INTEGER, hours_worked INTEGER, street_name TEXT, hours_left INTEGER, time_when_ill INTEGER, extra_worked_hours INTEGER, user_type TEXT,username TEXT, password TEXT)")

age_randomizingList = [1, 2, 3, 4, 6, 7, 8, 9, 10]
post_code_List = [1, 2, 3, 4, 6, 7, 8, 9]
myList = list(range(1, 101))

for i in range(1, 101):
    first_name = "FirstName{0}".format(i)
    second_name = "SecondName{0}".format(i)
    if i > 64:
        age = i-int(random.choice(age_randomizingList))
    elif i < 15:
        age = i+int(random.choice(age_randomizingList[:]))
    else:
        age = i
    city = "city{0}".format(i)
    post_code = ""
    for i in range(1, 6):
        post_code += "{0}".format(random.choice(post_code_List))
    post_code = int(post_code)
    salary = int(random.choice(list(range(1500, 4501))))
    street_name = "Street{0}".format(i)
    hours_worked = random.choice(list(range(5, 13)))
    hours_left = random.choice(list(range(1, 6)))
    time_when_ill = random.choice(list(range(1, 5)))
    extra_worked_hours = random.choice(list(range(10, 21)))
    user_type = random.choice(list(range(1, 4)))
    if user_type==1:
        user_type="admin"
    else:
        user_type="worker"
    x = random.choice(myList)
    username = "Username{0}".format(x)
    password = "Password{0}".format(x)
    del myList[myList.index(x)]

    params = (first_name, second_name, age, city, post_code, salary, hours_worked, street_name, hours_left, time_when_ill, extra_worked_hours, user_type,username, password)
    
    #database_cursor.execute("INSERT OR REPLACE INTO admins_workers VALUES (?,?,?, ?, ?,?,?, ?, ?,?,?, ?, ?)", params)
    database_cursor.execute("INSERT OR REPLACE INTO admins_workers VALUES ('{0}', '{1}',  {2}, '{3}', {4}, {5}, {6}, '{7}', '{8}', {9}, {10}, '{11}', '{12}', '{13}')".format(
        first_name,second_name,age,city,post_code, salary, hours_worked, street_name, hours_left, time_when_ill, extra_worked_hours, user_type, username, password
        ))
    

database.commit()

database_cursor.close()
database.close()

    

    
        
