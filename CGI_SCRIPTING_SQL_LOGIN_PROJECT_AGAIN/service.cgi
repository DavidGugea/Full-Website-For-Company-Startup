#!C:/jocuri david/python/python.exe
import cgi, cgitb, sqlite3, sys
cgitb.enable()
form=cgi.FieldStorage()

print("""
<!DOCTYPE html>
<html>
    <head>
        <title>
            Service
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

if "first_name" not in form or "second_name" not in form or "street_name" not in form or "city_name" not in form or "post_code" not in form or "email" not in form or "username" not in form or "password" not in form:
    print("""
    Please write correctly and fill in all the inputs boxes !
    </a></h1></header></body></html>
    """)
    sys.exit(0)
    
database = sqlite3.connect("PythonDatabase.db")
database_cursor = database.cursor()

database_cursor.execute("""
SELECT * FROM abos 
""")
users_list = []
for element in database_cursor:
    users_list.append(element)

#FORM VALUES 
first_name = form["first_name"].value 
second_name = form["second_name"].value 
city_name = form["city_name"].value 
post_code = form["post_code"].value 
street_name = form["street_name"].value 
email = form["email"].value 
username = form["username"].value 
password = form["password"].value 
#FORM VALUES

find_user = False 
userList = [] 
for element in users_list:
    if element[-2] == password and element[-3] == username:
        find_user = True 
        userList = element
    else:
        find_user = False 

if find_user == False:
    print("""
    The user couldn't be found in the database. Try again !
    </a></h1></header></body></html>
    """)
    sys.exit(0)
else:
    print("""
    The product succesfully has been sent to this adress 
    </a></h1></header></body></html>
    """)

amount_set = int(userList[-1])
amount_set += 1


database_cursor.execute("""
UPDATE abos SET amount = {2} WHERE username = '{0}' and password = '{1}' 
""".format(
    username,
    password,
    amount_set
))

database.commit()
database_cursor.close()
database.close()
