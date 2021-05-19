import hashlib
import csv
import pandas as pd
import logging

all_loggers = logging.getLogger(__name__)
# register_logger = logging.getLogger(__name__)
# product_logger = logging.getLogger(__name__)

all_loggers.setLevel(logging.INFO)
# -------create handlers------------
file_handler = logging.FileHandler('menu_log.log')
std_handler = logging.StreamHandler()

# --------set level for handlers -----------------
file_handler.setLevel(logging.INFO)
std_handler.setLevel(logging.DEBUG)

# -----------create format for handlers
s_format = logging.Formatter('%(asctime)s - %(levelname)s- %(message)s',datefmt='%d-%b-%y')
file_handler.setFormatter(s_format)

# ---------------add handler to logger------------------
all_loggers.addHandler(file_handler)
all_loggers.addHandler(std_handler)


class User:
    def __init__(self, username, password, status=True):
        self.username = username
        self.password = password
        self.status = status

    @staticmethod
    def register(username):
        """
            call it in user class
            :return: user object
            """
        file_path = "account.csv"
        df_account = pd.read_csv(file_path)
        list_username = list(df_account['username'])
        """
        just one admin can regster to system
        if admin_identity is empty, the user can register as an admin
        """

        # ------------check the username exist-----------
        while True:

            if username in list_username:
                print("username is exist")

            elif username not in list_username:
                try:
                    password = input("please enter password")

                    if username == '' or password == '':
                        print("try again...")
                    else:
                        # ---------------confirm the password -------------
                        try:
                            repassword = input("please enter password again")

                        except ArithmeticError:
                            print('invalid input,enter your username.\n')
                        except ValueError:
                            print('invalid input,enter a number.\n')
                        except TypeError:
                            print("enter suitable input")
                        else:
                            if password != repassword:
                                print("The invalid password")

                            else:
                                break
                except ArithmeticError:
                    print('invalid input,enter your username.\n')
                except ValueError:
                    print('invalid input,enter a number.\n')
                except TypeError:
                    print("enter suitable input")
            else:
                print("invalid requirement")

        # -----------hash_password == password------
        hash_password = hashlib.sha256(password.encode('utf8')).hexdigest()

        # -----------save to svg file--------------
        user = User(username, hash_password)
        user_info = [[user.username, user.password, user.status]]
        try:
            with open(file_path, 'a', newline='')as scv_file:
                csv_writer = csv.writer(scv_file)
                # writing the data row
                csv_writer.writerows(user_info)
        except:
            print("File error ")
        return user


    @staticmethod
    def login(username):
        flag = 0
        file_path = "account.csv"
        df_account = pd.read_csv(file_path)
        count = 0
        login_count = 0
        while flag == 0:  # for find
            try:
                with open(file_path, 'r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    # username = input("enter username: ")
                    for row in csv_reader:
                        if username == row[0]:
                            if row[2] == "True":
                                while login_count < 3:
                                    password = input("Enter password: ")
                                    hash_password = hashlib.sha256(password.encode('utf8')).hexdigest()
                                    if hash_password == row[1]:
                                        # print("\nyour login success!!\n")
                                        return True  # while
                                    else:
                                        print("wrong password!\n")
                                        login_count += 1

                                flag = 1
                                if login_count >= 3:
                                    # print("Sorry, your account blocked")
                                    df_account.loc[count - 1, 'status'] = "False"
                                    df_account.to_csv("account.csv", index=False)

                                return False  # for
                            else:
                                print("your account blocked")

                        count += 1  # next row
                    else:
                        print(f"Username dosent exist, please try again..\n")
                        continue
            except:
                print("File error  ")
    @staticmethod
    def change_password(username, old_password, new_password):
        change = pd.read_csv('account.csv')
        location = 0

        # tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
        try:
            with open('account.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                # csv_writer = csv.writer(tempfile, delimiter=',')

                for row in csv_reader:
                    if username == row[0]:
                        # old_password = input("enter your old password")
                        hash_old_password = hashlib.sha256(old_password.encode('utf8')).hexdigest()
                        if hash_old_password == row[1]:
                            # new_pass = input("what is new password:")
                            hash_password = hashlib.sha256(new_password.encode('utf8')).hexdigest()
                            row[1] = hash_password
                            """
                            !-----------------update password in file -----------------!
                            """
                            change.loc[location - 1, 'password'] = hash_password
                            change.to_csv('account.csv', index=False)
                        else:
                            print("your old password is wrong")
                            all_loggers.warning("wrong password was enter")
                        location += 1
                    else:
                        print("please try again")
                        all_loggers.warning("password dosent changed")
        except:
            print("File error ")

def is_admin(username):
    """
    check that user is admin or not.
    :return: True/False
    """
    Admin = pd.read_csv('username_datas.csv', usecols=['rule'])

    security_key = 1234
    try:
        select_user = int(input("""
                                    Are you
                                        1.admin
                                        2.customer?
                                        please inter your roll number"""))
    except ArithmeticError:
        print('invalid input,enter your username.\n')
    except ValueError:
        print('invalid input,enter a number.\n')
    except TypeError:
        print("enter suitable input")
    else:
        if select_user == 1:

            # ---------check security key------------
            try:
                user_security_key = int(input("For identify admin, please enter security key "))
            except ValueError:
                print('invalid input,enter a number.\n')
            except TypeError:
                print("enter suitable input")

            else:
                # --------- add user to the admin list for check that just one admin register or login ------------
                if len(Admin)<=1:
                    if security_key == user_security_key:

                        return True
                    else:
                        print("access denied")
                        all_loggers.warning("user was not admin")
                        return False
                else:
                    print("just one admin can register.")
                    return False

        else:
            return False


def add_uername_to_file(username ,rule ):
    with open('username_datas.csv', 'a')as scv_file:
        csv_reader=csv.DictWriter(scv_file,fieldnames=['username','rule',])
        csv_writer = csv.DictWriter(scv_file,fieldnames=[
        'username',
        'rule',

    ])
        # writing the data row

        csv_writer.writerow({
            'username':username , 'rule':rule
        })
