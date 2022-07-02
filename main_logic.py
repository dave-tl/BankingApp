from data_handler import password_changer, user_remove, transaction_handler, balance_handler


def user_interface(cur_usr, cur_pas=None):
    users = {}

    balance_handler()
    with open("bank.txt") as print_balance:
        print("current user : " + cur_usr)
        for line in print_balance:
            usr, mon = line.partition("-")[::2]
            users[usr.strip()] = str(mon)
            for k, v in users.items():
                if cur_usr == k:
                    money = v.strip()
        print("balance : " + money)
        print("\n(1) money transfer ")
        print("\n(2) change password ")
        print("\n(3) delete user ")
        print("\n(4) log out \n")

        interface_input = input("chose operation : ")
        if interface_input == "1":
            recipient = input("input recipient's name")
            amount = input("input amount")
            transaction_handler(cur_usr, recipient, amount)
            print(user_interface(cur_usr, cur_pas))

        elif interface_input == "2":
            password_changer(cur_usr)
            print("\n Password changed \n")
            user_interface(cur_usr, cur_pas)

        elif interface_input == "3":
            user_remove(cur_usr, cur_pas, money)
            print("\n user removed from data base \n")
            mainframe(status=False)

        elif interface_input == "4":
            mainframe(status=False)

        else:
            user_interface(cur_usr)


def bank(cur_usr, cur_pas):
    users = {}
    banks = {}
    with open("bank.txt", "a+") as check_if_bank_txt_exists:
        b_check = True
    with open('user.txt') as user_data:
        for line in user_data:
            usr, pas = line.partition("-")[::2]
            users[usr.strip()] = str(pas)
            for k, v in users.items():
                Username = k
            Money = ""
    with open('bank.txt') as bank_check:
        for line2 in bank_check:
            usr, mon = line2.partition("-")[::2]
            banks[usr.strip()] = str(pas)
            for key, val in banks.items():
                Username2 = key
    for Username in users:
        if Username not in banks:
            with open("bank.txt", "a+") as bank_data:
                bank_data.write(Username + '-' + Money + "\n")
                bank_data.close()
    user_interface(cur_usr, cur_pas)


def mainframe(status=False, cur_usr=None, cur_pas=None):
    if status is True:
        print("-" * 15 + "\n" + "Login Successful" + "\n" + "-" * 15)
        bank(cur_usr, cur_pas)

    else:
        print("||||welcome||||\n")
        login_or_register = input("login | register\n>:")
        if login_or_register in ["l", "login", "1"]:
            signin()
        elif login_or_register in ["r", "register", "2"]:
            signup()
        else:
            mainframe()


def signin():
    signin_users = {}

    with open('user.txt', "r") as user_data:
        for line in user_data:
            usr, pas = line.partition("-")[::2]
            signin_users[usr.strip()] = str(pas)

    def signin_username():
        print("\n" + "login" + "\n" + "-" * 15)
        Username = input("enter username: ")
        if Username != "":
            temp1 = ''
            temp2 = ''
            global c_usr
            c_usr = Username
            for k, v in signin_users.items():
                if k == Username:
                    cur_user = Username
                    temp1 = k
                    temp2 = v
            if temp1 == Username:
                def signin_password():
                    print(temp2.strip())
                    ps = input("password: ")
                    cur_pas = ps
                    if ps == temp2.strip():
                        mainframe(True, cur_user, cur_pas)

                    else:
                        print("wrong password")
                        signin_password()

                signin_password()
            else:
                signin_username()
        else:
            signin_username()
    signin_username()


def signup():
    with open("user.txt", "a+") as reg:
        Username = input("Create username: ")
        signup_users = {}
        with open('user.txt') as user_data:
            for line in user_data:
                usr, pas = line.partition("-")[::2]
                signup_users[usr.strip()] = str(pas)
                for k, v in signup_users.items():
                    if Username == k:
                        print("username taken!")
                        signup()

        def password():
            print("\nPassword should contain\n--------------------"
                  "\none capital letter \none lower case\none number "
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


mainframe()
