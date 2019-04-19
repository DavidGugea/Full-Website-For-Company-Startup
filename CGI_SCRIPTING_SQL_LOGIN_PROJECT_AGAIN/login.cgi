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
            .info-division{
                width: 30%;
                margin: auto;
                color: #444;
                font-family: cursive;
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
            #main-header h1, h2, h3, h4, h5, h6{
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

            .delete-user-div{
                position: absolute;
                top: 650px;
                left: 0px
            }
            .see-user-data-div{
                position: absolute;
                top: 650px;
                right: 0px;
            }
            .delete-user-div-2{
                position: absolute;
                top: 375px;
                left: 0px;
            }
            .see-user-data-div-2{
                position: absolute;
                top: 375px;
                right: 0px;
            }
            .change-user-data-div{
                position: absolute;
                top: 750px;
                left: 0px;
            }
            .add-user-div{
                position: absolute;
                top: 750px;
                right: 0px;
            }
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
            <h4>
                <a href="#" class="main-header-title-button">
""")

if "username" not in form or "password" not in form:
    print("""
    Please fill in all the input boxes
    </a></h1></header></body></html>
    """)
    sys.exit(0)

######################################################################################################

USER_TYPE = ""

######################################################################################################

data = open("UEC_CODE.bin", "rb") #         rb = read binary 
myList = []
while True:
    try:
        ECs = pickle.load(data)
        myList.append(ECs)
        continue 
    except:
        break 
    
if "UEC_code" not in form:
    USER_TYPE = "abo"
elif form["UEC_code"].value == myList[0]:
    USER_TYPE = "administrator"
elif form["UEC_code"].value == myList[1]:
    USER_TYPE = "worker"
elif form["UEC_code"].value == myList[-1]:
    USER_TYPE = "moderator"

login_username = form["username"].value 
login_password = form["password"].value 



#USER TYPE ABO ###################################################################################################
if USER_TYPE == "abo":
    #####
    #   PythonDatabase.db -- > abos 
    ####

    database = sqlite3.connect("PythonDatabase.db")
    database_cursor = database.cursor()

    ALL_USERS_LIST = [] 

    database_cursor.execute("SELECT * FROM abos")

    for element in database_cursor:
        ALL_USERS_LIST.append(element)
    
    user_find_BOOL = False 

    ########################################################################################################
    user_find_List = []
    ########################################################################################################

    for tuple_element in ALL_USERS_LIST:
        if tuple_element[-2] == login_password and tuple_element[-3] == login_username:
            user_find_BOOL = True 
            user_find_List = list(tuple_element)
            break 
        else:
            user_find_BOOL = False 
            continue 
        
    if user_find_BOOL == False:
        print("""
        This user couldn't be found, try again !
        </a></h1></header></body></html>
        """)
        sys.exit(0)
    else:
        print("""
        Hello, {0}. Welcome ! </a></h1></header></body></html>
        """.format(user_find_List[1]))
    
    #Need to print all ABO data +
    #Need to make form for updating ABO data 
    
    print("<div class='container'>")


    print("""
    <div class="user_data_div_html">
        First name: {0}<br><br>
        Second name: {1}<br><br>
        City name: {2}<br><br>
        Post code: {3}<br><br>
        Street name: {4}<br><br>
        Email: {5}<br><br>
        Username: {6}<br><br>
        Password: {7}<br><br>
        Amount of products buyed: {8}<br><br>
        <br><br><br>
    </div>
    """.format(
        user_find_List[0],
        user_find_List[1],
        user_find_List[2],
        user_find_List[3],
        user_find_List[4],
        user_find_List[5],
        user_find_List[6],
        user_find_List[7],
        user_find_List[8]
    ))

    print("""
    <div class="user_data_div_html">
        <p>
            Here is where you can change your data(adress/email etc.)
            You can write what you want in the input boxes, but when you click on Submit, make sure 
            that every input box it's filled. If there is no need to change something,
            write 'NONE' in the input box.
        </p>
    </div>
    <form action="abo_change.cgi">
        <input name="abo_change_first_name" class="input-box" placeholder="Change first name" type="text">
        <input name="abo_change_second_name" class="input-box" placeholder="Change second name" type="text">
        <br><br>
        <input name="abo_change_city_name" class="input-box" placeholder="Change city name" type="text">
        <input name="abo_change_post_code" class="input-box" placeholder="Change post code" type="text">
        <br><br>
        <input name="abo_change_street_name" class="input-box" placeholder="Change street name" type="text">
        <input name="abo_change_email" class="input-box" placeholder="Change email" type="text">
        <br><br>
        <input name="abo_change_username" class="input-box" placeholder="Change username" type="text">
        <input name="abo_change_password" class="input-box" placeholder="Change password" type="text">
        <br><br>
        <input value="{0}" name="MAIN_USERNAME_HTML" type="hidden">
        <input value="{1}" name="MAIN_PASSWORD_HTML" type="hidden">
        <input value="Submit" type="submit" class="submit-button">
    """.format(
        user_find_List[-3],
        user_find_List[-2]
    ))
    print("""
    <div style="margin-bottom: 250px"></div>
    """)
#USER TYPE ABO ###################################################################################################




#USER TYPE WORKER#################################################################################################
if USER_TYPE == "worker":
    MAIN_USERNAME_HTML = form["username"].value 
    MAIN_PASSWORD_HTML = form["username"].value 
    #Show the user(worker) all the data about him

    ###############################################################################
    workers_list = []
    user_list = []
    ###############################################################################

    database = sqlite3.connect("PythonDatabase.db")
    database_cursor = database.cursor()
    database_cursor.execute("SELECT * FROM admins_workers")
    
    for tuple_Element in database_cursor:
        if tuple_Element[-3] == "worker":
            workers_list.append(tuple_Element)
    
    for element in workers_list:
        if element[-1] == form["password"].value and element[-2] == form["username"].value:
            user_list = element 

    if user_list == []:
        print("""
        The username and the password don't match or they are wrong.
        Try again.
        </a></h1></header></body></html>
        """)
        sys.exit(0)
    #
    
    
    print("Welcome {0}. Have a nice day !</a></h1></header>".format(user_list[0]))
    print("<br><br>")
    print("""
    <div class="container">
        <div class="info-division">
        First name: {0}<br><br>
        Second name: {1}<br><br>
        Age: {2}<br><br>
        City: {3}<br><br>
        Post code: {4}<br><br>
        Salary: {5}<br><br>
        Hours worked (daily hours worked): {6}<br><br>
        Street name: {7}<br><br>
        Hours left: {8}<br><br>
        Time when ill (missing work because you were ill): {9}<br><br>
        Extra hours worked (extra pay hours): {10}<br><br>
        User type:{11}<br><br>
        Username: {12}<br><br>
        Password: {13}<br><br>
        </div>
    </div>
    </body></html>
    """.format(
        user_list[0],
        user_list[1],
        user_list[2],
        user_list[3],
        user_list[4],
        user_list[5],
        user_list[6],
        user_list[7],
        user_list[8],
        user_list[9],
        user_list[10],
        user_list[11],
        user_list[12],
        user_list[13]
    ))


#USER TYPE WORKER#################################################################################################







#USER TYPE ADMINISTRATOR##########################################################################################
if USER_TYPE == "administrator":
    database = sqlite3.connect("PythonDatabase.db")
    database_cursor = database.cursor()

    database_cursor.execute("SELECT * FROM admins_workers")
    all_admins_list = []
    for element in database_cursor:
        if element[-3] == "admin":
            all_admins_list.append(element)
    

    user_list = []

    #Checking if the user is in the admins list 
    for element in all_admins_list:
        if element[-1] == login_password and element[-2] == login_username:
            user_list = element 
            break 
        else:
            continue 

    if user_list == []:
        #The user couldn't be found !
        print("""
        The password and the username don't match.
        Try again !
        </a></h1></header></body></html>
        """)
        sys.exit(0)
    #

    print("""
    First name: {0}<br><br>
    Second name: {1}<br><br>
    Age: {2}<br><br>
    City: {3}<br><br>
    Post code: {4}<br><br>
    Salary: {5}<br><br>
    Hours worked: {6}<br><br>
    Street name: {7}<br><br>
    Hours left: {8}<br><br>
    Times when you were ill: {9}<br><br>
    Extra hours worked (extra pay hours): {10}<br><br>
    User type: {11}<br><br>
    Username: {12}<br><br>
    Password: {13}<br><br>
    """.format(
        user_list[0],
        user_list[1],
        user_list[2],
        user_list[3],
        user_list[4],
        user_list[5],
        user_list[6],
        user_list[7],
        user_list[8],
        user_list[9],
        user_list[10],
        user_list[11],
        user_list[12],
        user_list[13]
    ))

    #DIVISIONS for user            .delete-user-div             .see-user-data-div
    print("""
    <div class="delete-user-div">
        <section class="section-box">
            <h3>
                <a href="#" class="main-header-title-button">
                    Delete user 
                </a>
            </h3>
            <small>You have to write in the boxes below the username and the password of the user that you want 
            <br>
            to delete from the database</small>
            <br><br>
            <form action="admin_delete_user.cgi">
                <input class="input-box" type="text" placeholder="Username" name="delete_username"><br><br>
                <input class="input-box" type="text" placeholder="Password" name="delete_password"><br><br>
                <input class="submit-button" type="submit" value = "Delete user">
            </form>
        </section>
    </div>
    <div class="see-user-data-div">
        <section class="section-box">
            <h3>
                <a href="#" class="main-header-title-button">
                    Info box
                </a>
            </h3>
            <small>You have to write in the boxes below the username and the first name of the user that you want 
            <br>
            to get info from the database</small>
            <br><br>
            <form action="admin_user_info.cgi">
                <input class="input-box" type="text" placeholder="Username" name="info_username"><br><br>
                <input class="input-box" type="text" placeholder="First name" name="info_first_name"><br><br>
                <input class="submit-button" type="submit" value = "Info user">
            </form>
        </section>
    </div>
    """)
    #admin_delete_user.cgi
    #admin_user_info.cgi

#USER TYPE ADMINISTRATOR##########################################################################################

#USER TYPE MODERATOR##############################################################################################
if USER_TYPE == "moderator":
    pickle_list = []
    file = open('moderator_us_ps_binary.bin', 'rb')
    while True:
        try:
            pickle_list.append(pickle.load(file))
        except:
            break 

    should_enter_username = pickle_list[0]
    should_enter_password = pickle_list[1]
    file.close()

    if login_username != should_enter_username or login_password != should_enter_password:
        print("""
        The username and password that you are trying to enter, are wrong.
        Try again !
        </a></h1></header></body></html>
        """)
        sys.exit(0)
    
    #

    print("<h1>Welcome David !</h1><br>")
    pickle_list = []
    file = open("UEC_CODE.bin", "rb")
    while True:
        try:
            pickle_list.append(pickle.load(file))
        except:
            break 
    
    admin_EC_code = pickle_list[0]
    worker_EC_code = pickle_list[1]
    moderator_EC_code = pickle_list[2]
    
    print("""
    <h3>Admin EC code -- > {0}<br><br>
    Worker EC code -- > {1}<br><br>
    Moderator EC code -- > {2}<br><br></h3>
    """.format(
        admin_EC_code,
        worker_EC_code,
        moderator_EC_code
    ))
    # delete-user-div-2
    # see-user-data-div-2

    print("""
        <div class="delete-user-div-2">
            <h3>
                <a href="#" class="main-header-title-button">
                    Delete user 
                </a>
            </h3>
            <small>You have to write in the boxes below the username and the password of the user that you want 
            <br>
            to delete from the database</small>
            <br><br>
            <form action="moderator_delete_user_SCRIPT.cgi">
                <input name="username" class="input-box" type="text" placeholder="Delete Username">
                <input name="password" class="input-box" type="text" placeholder="Delete Password">
                <br><br>
                <input type="submit" class="submit-button">
            </form>
        </div>
        <div class="see-user-data-div-2">
            <h3>
                <a href="#" class="main-header-title-button">
                    See user info
                </a>
            </h3>
            <small>You have to write the first name and the username of the user that you want to get informations from
            </small>
            <br><br><br>
            <form action="moderator_user_info_SCRIPT.cgi">
                <input name="username" class="input-box" type="text" placeholder="Username">
                <input name="first_name" class="input-box" type="text" placeholder="First name">
                <br><br>
                <input type="submit" class="submit-button">
            </form>
        </div>
        <div class="change-user-data-div">
            <h3>
                <a href="#" class="main-header-title-button">
                    Change user data 
                </a>
            </h3>
            <small>You have to write in every input box the things that you want to change.
            <br>Remember that the username cannot be changed ! <br>If there is no need to change something, write 
            "NONE". You can also change the username. But first you have to write it</small>
            <br><br>
            <form action="moderator_change_data_SCRIPT.cgi">
                <input name="find_username" class="input-box" type="text" placeholder="Username !">
                
                <br><br>
                <input name="first_name" class="input-box" type="text" placeholder = "Change first name">
                <input name="second_name" class="input-box" type="text" placeholder = "Change second name">
                <br><br>
                <input name="age" class="input-box" type="text" placeholder = "Change age">
                <input name="city" class="input-box" type="text" placeholder = "Change city">
                <br><br>
                <input name = "post_code" class="input-box" type="text" placeholder = "Change post code">
                <input name = "salary" class="input-box" type="text" placeholder = "Change salary">
                <br><br>
                <input name="hours_worked" class="input-box" type="text" placeholder="Change hours worked(daily)">
                <input name="street_name" class="input-box" type='text' placeholder = "Change street name">
                <br><br>
                <input name="hours_left" class="input-box" type="text" placeholder = "Change hours left">
                <input name="time_when_ill" class="input-box" type="text" placeholder = 'Change times when the worker/admin was ill'>
                <br><br>
                <input name="extra_worked_hours" class="input-box" type="text" placeholder = "Change extra hours worked, extra pay hours">
                <input name="user_type" class="input-box" type="text" placeholder="Change the user type">
                <br><br>
                <input name="change_username" class="input-box" type="text" placeholder = "Change username">
                <input name="password" class="input-box" type="text" placeholder = "Change password">
                <br><br>
                
                <input type="submit" class="submit-button" value="Submit">
                <br><br><br><br><br>
            </form>
        </div>
        <div class="add-user-div">
            <h3>
                <a href="#" class="main-header-title-button">
                    Add worker or admin 
                </a>
            </h3>
            <small>
            You have to fill in all the input boxes to add the user in our database.
            </small>
            <br><br><br><br>
            <form action="moderator_add_user_SCRIPT.cgi">
                <input name="first_name" class="input-box" type="text" placeholder = "Add first name">
                <input name="second_name" class="input-box" type="text" placeholder = "Add second name">
                <br><br>
                <input name="age" class="input-box" type="text" placeholder = "Add age">
                <input name ="city" class="input-box" type="text" placeholder = "Add city">
                <br><br>
                <input name="post_code" class="input-box" type="text" placeholder="Add post code">
                <input name="salary" class="input-box" type="text" placeholder="Add salary">
                <br><br>
                <input name="hours_worked" class="input-box" type="text" placeholder = "Add hours worked(daily)">
                <input name="street_name" class="input-box" type="text" placeholder = "Add street name">
                <br><br>
                <input name="hours_left" class="input-box" type="text" placeholder = "Add hours left">
                <input name="time_when_ill" class="input-box" type="text" placeholder = "Add time when ill">
                <br><br>
                <input name="extra_worked_hours" class="input-box" type="text" placeholder = "Add extra worked hours">
                <input name="user_type" class="input-box" type="text" placeholder = "Add user type">
                <br><br>
                <input name="username" class="input-box" type="text" placeholder = "Add username">
                <input name="password" class="input-box" type="text" placeholder = "Add password">
                <br><br>
                <input type="submit" value = "Submit" class="submit-button">
                <br><br><br><br><br>
            </form>
        </div>
    </body>
</html>
    """)
#USER TYPE MODERATOR##############################################################################################














    