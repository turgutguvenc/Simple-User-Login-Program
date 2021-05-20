print("""
*********************************
User Login Program
*********************************

""")
sys_user_name = "tgvenc"
sys_password ="123456"
number_of_attemps = 3
while True:
    user_name = input("Please Enter Your User Name: ")
    password = input("Please Enter Your Password: ")

    if (sys_user_name != user_name) and (password == sys_password):
        print("Username is incorrect")
        number_of_attemps -= 1

    elif (sys_user_name == user_name) and (password != sys_password):
        print("Password is incorrect")
        number_of_attemps -= 1

    elif (sys_user_name != user_name) and (password != sys_password):
        print("Username and password are incorrect")
        number_of_attemps -= 1
    else:
        print("Welcome the system....")
        break
    if number_of_attemps ==0:
        break