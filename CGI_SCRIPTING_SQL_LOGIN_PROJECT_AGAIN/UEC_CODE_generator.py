import pickle, os, sys, random

if os.path.exists("UEC_CODE.bin"):
    while True:
        question = input("Do you want to rewrite the UEC code ?  -- > ")

        if question == "yes" or question == "Yes":
            #break, no sys.exit(0), no console close (;)
            break
        else:
            #Show the admin the UEC code for the worker/admins/moderator
            a = []
            pickle_UEC = open("UEC_CODE.bin", "rb") #                     rb = read binary, because .bin
            while True:
                try:
                    data = pickle.load(pickle_UEC)
                    a.append(data)
                except:
                    break

            ###########################################################################################################################
            #   --FIRST ELEMENT FROM THE UEC CODE IS admin -- SECOND ELEMENT FROM THE UEC CODE IS worker --  THIRD ELEMENT FROM THE UEC CODE IS moderator #
            ###########################################################################################################################
            for i in range(5):
                print() 
            print("Administrators EC -- > {0}".format(a[0]))
            print("Workers EC -- > {0}".format(a[1]))
            print("Moderator EC -- > {0}".format(a[2]))
            for i in range(5):
                print()

#generate EC codes for ADMINS, WORKERS, MODERATOR
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#ECs
admin_EC = ""
worker_EC = ""
moderator_EC = ""
#ECs

a = []
for i in range(1, 10):
    a.append(i)

for i in range(10):
    admin_EC += "{0}".format(random.choice(alpha))
    worker_EC += "{0}".format(random.choice(alpha))
    moderator_EC += "{0}".format(random.choice(alpha))

for i in range(10):
    admin_EC += "{0}".format(random.choice(a))
    worker_EC += "{0}".format(random.choice(a))
    moderator_EC += "{0}".format(random.choice(a))

for i in range(10):
    admin_EC += "{0}".format(random.choice(alpha))
    worker_EC += "{0}".format(random.choice(alpha))
    moderator_EC += "{0}".format(random.choice(alpha))

for i in range(10):
    admin_EC += "{0}".format(random.choice(a))
    worker_EC += "{0}".format(random.choice(a))
    moderator_EC += "{0}".format(random.choice(a))

data = open("UEC_CODE.bin", "wb") #                     wb = write binary, because .bin

#Dump ECs into binary file                                                                                                                                          pickle.dump(obj, file)

pickle.dump(admin_EC, data)
pickle.dump(worker_EC, data)
pickle.dump(moderator_EC, data)

data.close()
















    
