#!C:/jocuri david/python/python.exe
import cgi, cgitb, sqlite3, sys, pickle
cgitb.enable()
form=cgi.FieldStorage()

print("""
<!DOCTYPE html>
<html>
    <head>
        <title>
            Login
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

            .user_data_div_html{
                text-align: center;
                font-family: cursive;
                color: #444;
            }
            
            .container form{
                text-align: center;
            }
            
                /* BOXES */
            .input-box{
                margin: 0px;
                border: 3px #999 solid;
                background-color: #333;
                color: #fff;
                font-family: cursive;
                padding: 5px;
                width: 200px;
            }
            .input-box:hover{
                border: 3px #333 solid;
                background-color: #999;
                color: #fff;
            }
            .input-box:active{
                border: 3px #999 solid;
                background-color: #444 solid;
                color: rgb(17, 138, 112);
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            }
                /* BOXES */

                /* SUBMIT BUTTON */
            .submit-button{
                margin: 0px;
                border: 3px #999 solid;
                background-color: #222;
                color: #fff;
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
                padding: 10px;
            }
            .submit-button:hover{
                font-family: cursive;
                border: 3px #222 solid;
                color: #999;
                background-color: #fff;
                padding: 11px;
            }
            .submit-button:active{
                font-family: impact;
                border: 3px #555 solid;
                color: dimgray;
                background-color: dodgerblue;
            }
                /* SUBMIT BUTTON */

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

if "abo_change_first_name" not in form or "abo_change_second_name" not in form or "abo_change_city_name" not in form or "abo_change_post_code" not in form or "abo_change_street_name" not in form or "abo_change_email" not in form or "abo_change_username" not in form or "abo_change_password" not in form:
    print("""
    Please fill in all the input boxes. Try again !
    </a></h1></header></body></html>
    """)
    sys.exit(0)


######################################################################################
#TAKING THE HIDDEN inputs WITH INTRO USERNAME+PASSWORD 
######################################################################################

global MAIN_USERNAME
global MAIN_PASSWORD

MAIN_USERNAME = str(form["MAIN_USERNAME_HTML"].value) 
MAIN_PASSWORD = str(form["MAIN_PASSWORD_HTML"].value) 

#######################################################################################

####
#SET EXAMPLE: UPDATE abos SET x=y WHERE username=MAIN_USERNAME, MAIN_PASSWORD
####

database = sqlite3.connect("PythonDatabase.db")
database_cursor = database.cursor()

if form["abo_change_first_name"].value != "NONE":
    database_cursor.execute("UPDATE abos SET first_name = '{0}' WHERE username = '{1}' AND password = '{2}'".format(
        form["abo_change_first_name"].value,
        MAIN_USERNAME,
        MAIN_PASSWORD
    ))
if form["abo_change_second_name"].value != "NONE":
    database_cursor.execute("UPDATE abos SET second_name = '{0}' WHERE username = '{1}' AND password = '{2}'".format(
        form["abo_change_second_name"].value,
        MAIN_USERNAME,
        MAIN_PASSWORD
    ))
if form["abo_change_city_name"].value != "NONE":
    database_cursor.execute("UPDATE abos SET city_name = '{0}' WHERE username = '{1}' AND password = '{2}'".format(
        form["abo_change_city_name"].value,
        MAIN_USERNAME,
        MAIN_PASSWORD
    ))
if form["abo_change_post_code"].value != "NONE":
    database_cursor.execute("UPDATE abos SET post_code = '{0}' WHERE username='{1}' AND password='{2}'".format(
        form["abo_change_post_code"].value,
        MAIN_USERNAME,
        MAIN_PASSWORD
    ))
if form["abo_change_street_name"].value != "NONE":
    database_cursor.execute("UPDATE abos SET street_name = '{0}' WHERE username = '{1}' AND password='{2}'".format(
        form["abo_change_street_name"].value,
        MAIN_USERNAME,
        MAIN_PASSWORD
    ))
if form["abo_change_email"].value != "NONE":
    database_cursor.execute("UPDATE abos SET email = '{0}' WHERE username = '{1}' AND password='{2}'".format(
        form["abo_change_email"].value,
        MAIN_USERNAME,
        MAIN_PASSWORD
    ))
if form["abo_change_username"].value != "NONE":
    database_cursor.execute("UPDATE abos SET username = '{0}' WHERE username = '{1}' AND password='{2}'".format(
        form["abo_change_username"].value,
        MAIN_USERNAME,
        MAIN_PASSWORD
    ))
if form["abo_change_password"].value != "NONE":
    database_cursor.execute("UPDATE abos SET password = '{0}' WHERE username='{1}' AND password = '{2}'".format(
        form["abo_change_password"].value,
        MAIN_USERNAME,
        MAIN_PASSWORD
    ))
database.commit()

database_cursor.close()
database.close()

find_NONE = []
find_NONE.append(form["abo_change_first_name"].value)
find_NONE.append(form["abo_change_second_name"].value)
find_NONE.append(form["abo_change_city_name"].value)
find_NONE.append(form["abo_change_post_code"].value)
find_NONE.append(form["abo_change_street_name"].value)
find_NONE.append(form["abo_change_email"].value)
find_NONE.append(form["abo_change_username"].value)
find_NONE.append(form["abo_change_password"].value)

find_NONE_BOOLEAN = False 

for element in find_NONE:
    if element == "NONE":
        find_NONE_BOOLEAN = False 
        continue 
    if element != "NONE":
        find_NONE_BOOLEAN = True 
        break 

if bool(find_NONE_BOOLEAN) == True:
    print("""
    The data has been succesfully changed !
    </a></h1></header></body></html>
    """)
elif bool(find_NONE_BOOLEAN) == False:
    print("""
    Nothing has been changed !
    </a></h1></header></body></html>
    """)






































