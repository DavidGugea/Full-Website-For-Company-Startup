import pickle, sys, os, random

if os.path.exists('moderator_us_ps_binary.bin'):
    while True:
        question = input("The binary file already exists. Would you like to rewrite it ? -- > ")

        if question == "yes" or question == "Yes":
            break
        elif question == "no" or question == "no":
            file = open("moderator_us_ps_binary.bin", "rb") #               rb = read binary
            all_file_list = []

            while True:
                try:
                    all_file_list.append(pickle.load(file))
                    continue 
                except:
                    break

            print("Username -- > {0}".format(all_file_list[0]))
            print("Password -- > {0}".format(all_file_list[1]))

            for i in range(5):
                print()
            
            end_input = input("Press any key to end the programm.  ")
            sys.exit(0)
        else:
            for i in range(3):
                print()

            print("Please answer correctly to the question !")
            print("Try again !")

            for i in range(3):
                print()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

username = ""
password = ""
#1
for i in range(10):
    username += random.choice(alpha)
    password += random.choice(alpha)
#2
for i in range(10):
    username += str(random.choice(list(range(1, 10))))
    password += str(random.choice(list(range(1, 10))))
#3
for i in range(10):
    username += random.choice(alpha)
    password += random.choice(alpha)
#4
for i in range(10):
    username += str(random.choice(list(range(1, 10))))
    password += str(random.choice(list(range(1, 10))))
#5
for i in range(10):
    username += random.choice(alpha)
    password += random.choice(alpha)
#6
for i in range(10):
    username += str(random.choice(list(range(1, 10))))
    password += str(random.choice(list(range(1, 10))))
#7
for i in range(10):
    username += random.choice(alpha)
    password += random.choice(alpha)
#8
for i in range(10):
    username += str(random.choice(list(range(1, 10))))
    password += str(random.choice(list(range(1, 10))))
#9
for i in range(10):
    username += random.choice(alpha)
    password += random.choice(alpha)
#10
for i in range(10):
    username += str(random.choice(list(range(1, 10))))
    password += str(random.choice(list(range(1, 10))))

data = open("moderator_us_ps_binary.bin", "wb") #wb = write binary
pickle.dump(username, data)
pickle.dump(password, data)

data.close()



