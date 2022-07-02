def welcome(status=False):
    if status is True:
        print("-" * 15 + "\n" + "Login Successful" + "\n" + "-" * 15)

    else:
        print("||||welcome||||\n")
        login_or_register = input("login | register\n>:")
        if login_or_register in ["l", "login", "1"]:
            signin()
        elif login_or_register in ["r", "register", "2"]:
            signup()
        else:
            welcome()


def signin():
    users = {}

    with open('user.txt', "r") as user_data:
        for line in user_data:
            usr, pas = line.partition("-")[::2]
            users[usr.strip()] = str(pas)

    def signin_password():
        print(temp2.strip())
        ps = input("password: ")
        if ps == temp2.strip():
            welcome(True)

        else:
            print("wrong password")
            signin_password()

    def signin_username():
        Username = input("enter username: ")
        temp1 = ''
        for k, v in users.items():
            if k == Username:
                temp1 = k
                global temp2
                temp2 = v
        if temp1 == Username:
            signin_password()
        else:
            signin_username()

    signin_username()


def signup():
    with open("user.txt", "a+") as reg:
        Username = input("Create username: ")
        users = {}
        with open('user.txt') as user_data:
            for line in user_data:
                usr, pas = line.partition("-")[::2]
                users[usr.strip()] = str(pas)
                for k, v in users.items():
                    if Username == k:
                        print("username taken!")
                        signup()

        def password():
            print("\nPassword should contain\n--------------------\none capital letter \none lower case\none number "
                  "\nshould be at least 8 characters\n")
            Password = input("Create password: ")
            Password1 = input("Repeat password: ")
            alphabet = "qwertyuiopasdfghjklzxcvbnm"
            if Password == Username:
                password()
            if len(Password) < 8:
                print("!!!password should contain at least 8 characters!!!")
                password()
            if Password != Password1:
                print("!!!passwords don't match!!!")
                password()
            ck = []
            ck_up = []
            ck_counter = 0
            ck_up_counter = 0
            for char in Password:
                if char in alphabet:
                    ck.append(char)
            for char in Password:
                if char in alphabet.upper():
                    ck_up.append(char)

            for i in ck:
                ck_counter += 1
            for i in ck_up:
                ck_up_counter += 1
            if ck_counter < 1:
                print("!!!passwords must contain lower-case letters!!!")
                password()
            if ck_up_counter < 1:
                print("!!!passwords must contain capital letters!!!")
                password()
            else:
                reg.write(Username + '-' + Password + "\n")
                print("success")
                reg.close()
                signin()

        password()
    signup()


welcome()
