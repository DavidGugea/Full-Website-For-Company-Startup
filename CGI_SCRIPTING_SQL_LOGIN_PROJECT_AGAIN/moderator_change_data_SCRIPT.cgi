#!C:/jocuri david/python/python.exe
import cgi, cgitb, sqlite3, sys
cgitb.enable()
form=cgi.FieldStorage()

print("""
<!DOCTYPE html>
<html>
    <head>
        <title>
            Change data
        </title>
        <link href="css/register.css" rel="stylesheet" type="text/css">
        <meta charset="utf-8">
        <meta description="Service Website">
        <style>
            body{
                margin: 0px;
            }
            /* Set margins to 0 for body

            /* GLOBAL CLASSES */

            .container{
                width: 80%;
                margin: auto;
            }
            .clr{
                clear: both;
            }

            /* GLOBAL CLASSES */

            /* THE NAVBAR */

            #navbar{
                background-color: #333;
                position: relative;
                margin: 0px;
                width: 100%;
            }
            #navbar h3{
                margin: 0px;
            }
                /*navbar title button*/
            .navbar-title-button{
                text-decoration: none;
                margin-bottom: 0px;
                text-transform: none;
                color: #fff;
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            }
            .navbar-title-button:hover{
                color: #999;
            }
            .navbar-title-button:active{
                color: chartreuse;
            }
                /*navbar title button*/

                /* navbar links */
            #navbar ul{
                list-style: none;
            }
            #navbar ul li{
                display: inline;
                position: absolute;
            }
            #navbar ul li:nth-child(1){
                right: 0%;
                top: 0px;
            }
            #navbar ul li:nth-child(2){
                right: 10%;
                top: 0px;
            }
            #navbar ul li:nth-child(3){
                right: 20%;
                top: 0px;
            }
            #navbar ul li:nth-child(4){
                right: 30%;
                top: 0px;
            }
                /* navbar links */

                /* the link button */
            .link-button{
                text-decoration: none;
                text-transform: none;
                color: #fff;
                font-family: cursive;
            }
            .link-button:hover{
                color: #888;
                border: #999 solid;
            }
            .link-button:active{
                color: rgb(55, 113, 167);
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            }
                /* the link button
            /* THE NAVBAR */ 

            /* TITLE */
            #main-header{
                width: 100%;
                margin: 0px;
                margin-top: 5px;
                margin-bottom: 80px;
            }
            #main-header h1{
                text-align: center;
            }
            .main-header-title-button{
                text-decoration: none;
                text-transform: none;
                color: #333;
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            }
            .main-header-title-button:hover{
                font-family: cursive;
                color: rosybrown;
            }
            .main-header-title-button:active{
                font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
                color: #999;
            }
            /* TITLE */
        </style>
    </head>
    <body>
        <!-- THE NAVBAR/ BEGINNING PART -->
        <nav id="navbar">
            <h3><a href="#" class="navbar-title-button">Python GmbH</a></h3>
            <ul>
                <li><a href="http://localhost/Python36/CGI_SCRIPTING_SQL_LOGIN_PROJECT_AGAIN/service.html" class="link-button">Service</a></li>
                <li><a href="http://localhost/Python36/CGI_SCRIPTING_SQL_LOGIN_PROJECT_AGAIN/register.html" class="link-button">Register</a></li>
                <li><a href="http://localhost/Python36/CGI_SCRIPTING_SQL_LOGIN_PROJECT_AGAIN/login.html" class="link-button" target='_blank'>Login</a></li>
                <li><a href="http://localhost/Python36/CGI_SCRIPTING_SQL_LOGIN_PROJECT_AGAIN/index.html" class="link-button">Home</a></li>
            </ul>
        </nav>
        <!-- THE NAVBAR/ BEGINNING PART -->

        <!-- Title -->

        <header id='main-header'>
            <h1>
                <a href="#" class="main-header-title-button">
""") 

if "find_username" not in form or "first_name" not in form or "second_name" not in form or "age" not in form or "city" not in form or "post_code" not in form or "salary" not in form or "hours_worked" not in form or "street_name" not in form or "hours_left" not in form or "time_when_ill" not in form or "extra_worked_hours" not in form or "user_type" not in form or "change_username" not in form or "password" not in form:
    print("""
    Please fill in all the input boxes! Try again !
    """)
    sys.exit(0)

database = sqlite3.connect("PythonDatabase.db")
database_cursor = database.cursor()

database_cursor.execute("SELECT * FROM admins_workers")

all_List = []

for tuple_element in database_cursor:
    all_List.append(tuple_element)

user_list = []

for data_list in all_List:
    if data_list[-2] == form["find_username"].value:
        user_list = data_list 
        break 
    else:
        continue 

if user_list == []:
    print("""
    The user couldn't be found in our database. Try again !
    """)
    sys.exit(0)

################# FORM VALUES #################

find_username = form["find_username"].value

first_name = form["first_name"].value  #1
change_second_name = form["second_name"].value  #2
change_age = form["age"].value  #3
change_city = form["city"].value #4
change_post_code = form["post_code"].value #5
change_salary = form["salary"].value #6
change_hours_worked = form["hours_worked"].value #7
change_street_name = form["street_name"].value #8
change_hours_left = form["hours_left"].value  #9
change_time_when_ill = form["time_when_ill"].value #12 
change_extra_worked_hours = form["time_when_ill"].value  #13
change_user_type = form["user_type"].value #14
change_username = form["change_username"].value #15
change_password = form["password"].value #16

################# FORM VALUES #################

print("""
The user data has been sucesfully changed !
""")

if first_name != "NONE":
    database_cursor.execute("UPDATE admins_workers SET first_name = '{0}' WHERE username = '{1}'".format(
        first_name,
        find_username
    ))

def change_data(main_value, set_value, type):
    if set_value != "NONE":
        if type=="string":
            database_cursor.execute("UPDATE admins_workers SET {0} = '{1}' WHERE username='{2}'".format(
                main_value,
                set_value,
                find_username 
            ))
        elif type=="integer":
            database_cursor.execute("UPDATE admins_workers SET {0} = {1} WHERE username='{2}'".format(
                main_value,
                set_value,
                find_username 
            ))            

#######################################################################################
change_data('second_name', change_second_name, "string")
change_data('age', change_age, "integer")
change_data('city', change_city, "string")
change_data('post_code', change_post_code, "integer")
change_data('salary', change_salary, "integer")
change_data('hours_worked', change_hours_worked, "integer")
change_data('street_name', change_street_name, "string")
change_data('hours_left', change_hours_left, "integer")
change_data('time_when_ill', change_time_when_ill, "integer")
change_data('extra_worked_hours', change_extra_worked_hours, "integer")
change_data('user_type', change_user_type, "string")
change_data('username', change_username, "string")
change_data('password', change_password, "string")
##################### ##################################################################

database.commit()
database_cursor.close()
database.close()