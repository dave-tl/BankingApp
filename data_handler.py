# error checking

# user removal

def user_remove(user, cur_pas, money):
    with open("user.txt", "r") as f:
        lines = f.readlines()
    with open("user.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != (user + "-" + cur_pas):
                f.write(line)
    with open("bank.txt", "r") as f:
        lines = f.readlines()
    with open("bank.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != (user + "-" + money):
                f.write(line)

        return


# Password change

def password_changer(user):
    def password_pass():
        print("\nPassword should contain\n--------------------"
              "\none capital letter \none lower case\none number "
              "\nshould be at least 8 characters\n")
        Password = input("Create password: ")
        Password1 = input("Repeat password: ")
        alphabet = "qwertyuiopasdfghjklzxcvbnm"
        if Password == user:
            password_pass()
        if len(Password) < 8:
            print("!!!password should contain at least 8 characters!!!")
            password_pass()
        if Password != Password1:
            print("!!!passwords don't match!!!")
            password_pass()
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
            password_pass()
        if ck_up_counter < 1:
            print("!!!passwords must contain capital letters!!!")
            password_pass()
        else:

            users = {}
            with open("user.txt") as edit_password:
                for line in edit_password:
                    usr, password = line.partition("-")[::2]
                    users[usr.strip()] = str(password)
                for k1, v1 in users.items():
                    if user == k1.strip():
                        t_update = Password
                        up_dict = {k1: t_update}
                        users.update(up_dict)
            with open("user.txt", "a") as trunc:
                trunc.truncate(0)
            for k, v in users.items():
                with open("user.txt", "a") as user_data:
                    user_data.write(k + '-' + str(v).strip() + "\n")
            return

    password_pass()


# transaction handler

def transaction_handler(f, t, amount):
    users = {}
    with open("bank.txt") as edit_balance:
        for line in edit_balance:
            usr, mon = line.partition("-")[::2]
            users[usr.strip()] = str(mon)
        for k, v in users.items():
            if f == k.strip():
                if int(amount) < int(v):
                    f_update = int(v.strip()) - int(amount)
                    up_dict = {k: f_update}
                    users.update(up_dict)
                else:
                    return print("\ninsufficient balance\n")

        for k1, v1 in users.items():
            if t == k1.strip():
                t_update = int(v1.strip()) + int(amount)
                up_dict = {k1: t_update}
                users.update(up_dict)
    with open("bank.txt", "a") as trunc:
        trunc.truncate(0)
    for k, v in users.items():
        with open("bank.txt", "a") as bank_data:
            bank_data.write(k + '-' + str(v).strip() + "\n")


# balance handling for new users

def balance_handler():
    users = {}
    with open("bank.txt") as edit_balance:
        for line in edit_balance:
            usr, mon = line.partition("-")[::2]
            users[usr.strip()] = str(mon)
        for k, v in users.items():
            if "" == v.strip():
                up_dict = {k: "0\n"}
                users.update(up_dict)
    with open("bank.txt", "a") as trunc:
        trunc.truncate(0)
    for k, v in users.items():
        with open("bank.txt", "a") as bank_data:
            bank_data.write(k + '-' + v)
