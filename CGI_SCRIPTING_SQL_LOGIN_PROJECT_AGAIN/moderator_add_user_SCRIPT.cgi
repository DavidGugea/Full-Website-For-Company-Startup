#!C:/jocuri david/python/python.exe
import cgi, cgitb, sqlite3, sys
cgitb.enable()
form=cgi.FieldStorage()

print("""
<!DOCTYPE html>
<html>
    <head>
        <title>
            Add user
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

if "first_name" not in form or "second_name" not in form or "age" not in form or "city" not in form or "post_code" not in form or "salary" not in form or "hours_worked" not in form or "street_name" not in form or "hours_left" not in form or "time_when_ill" not in form or "extra_worked_hours" not in form or "user_type" not in form or "username" not in form or "password" not in form:
    print("""
    You have to fill in all the input boxes !
    Try again !
    """)
    sys.exit(0)

database = sqlite3.connect("PythonDatabase.db")
database_cursor = database.cursor()

# FORM VALUES #

first_name = form["first_name"].value  #0
second_name = form["second_name"].value #1
age = form["age"].value #2
city = form["city"].value #3
post_code = form["post_code"].value #4
salary = form["salary"].value #5
hours_worked = form["hours_worked"].value #6
street_name = form["street_name"].value #7
hours_left = form["hours_left"].value #8
time_when_ill = form["time_when_ill"].value #9  
extra_worked_hours = form["extra_worked_hours"].value #10  
user_type = form["user_type"].value #11
username = form["username"].value #12
password = form["password"].value #13

# FORM VALUES #


database_cursor.execute("INSERT INTO admins_workers VALUES ('{0}','{1}', {2}, '{3}', {4}, {5}, {6}, '{7}', {8}, {9}, {10}, '{11}', '{12}', '{13}')".format(
    first_name,
    second_name,
    age,
    city,
    post_code,
    salary,
    hours_worked,
    street_name,
    hours_left,
    time_when_ill,
    extra_worked_hours,
    user_type,
    username,
    password
))

database.commit()

database_cursor.close()
database.close()

print("""
The user has been sucesfully added in the database !
Have a nice day !
""")