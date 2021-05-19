import user
from Product import Products
from admin import Admin
from customer import Customer
from user import *
import pandas as pd
import logging

# logging.basicConfig(level=logging.DEBUG, filename='storeAccount.log', filemode='a',
#                     format='%(asctime)s - %(levelname)s- %(message)s',datefmt='%d-%b-%y')


def menu():
    while True:
        print("************ Welcome to store accounting menu **************\n")
        """
        notice that after register or login user can change password and logout
        """
        # -----------main menu----------------------
        try:
            choice = input("""
                              A: Register
                              B: Login
                              
                              Please enter your choice: """)

        except ArithmeticError:
            print('invalid input,enter your choice.\n')
            all_loggers.error("Exception occured, user enter invalid input", exc_info=True)
        except ValueError:
            print('invalid input,enter "A" or "B".\n')
            all_loggers.error("Exception occured, user enter invalid input in menu", exc_info=True)
        except TypeError:
            print("enter suitable input")
            all_loggers.error("Exception occured, user enter invalid input", exc_info=True)

        else:
            # --------------------- register -----------------
            if choice == 'a' or choice == 'A':
                try:
                    username = input("please enter username:")
                    new_user = User.register(username)

                except ArithmeticError:
                    print('invalid input,enter your username.\n')

                # --------<end> Register ----------
                else:
                    if is_admin(new_user) == True:
                        try:
                            with open('Products.csv', 'r') as read_file:
                                product_file = csv.DictReader(read_file)
                                for row in product_file:

                                    if row['amount'] == "0":

                                        print(f"--->{row['name']} is zero.")

                        except:
                            print("file error")
                        else:
                            add_uername_to_file(new_user.username, 'Admin')
                            all_loggers.info("Admin is login right now!")
                            admin_menu()
                    else:
                        add_uername_to_file(new_user.username, 'Customer')
                        customer_menu()

            # -----------------------login--------------------
            elif choice == 'b' or choice == 'B':
                all_users = pd.read_csv('username_datas.csv', usecols=['username'])
                try:
                    username = input("please enter username:")
                    if username in all_users:

                        user_ = User.login(username)
                        if user_ == True:
                            print("\nyour login success!!\n")
                            if is_admin(user_) == True:

                                """
                                alert to admin the products that count of them is zero .
                                """
                                try:
                                    with open('Products.csv', 'r') as read_file:
                                        product_file = csv.reader(read_file)
                                        for item in product_file:
                                            if int(item[4]) ==" 0":
                                                print(f"------> {item[1]} is finished <--------")
                                                all_loggers.info(f"{item[1]} is finished")
                                            else:
                                                pass

                                except:
                                    print("file error")
                                else:
                                    all_loggers.info("Admin is login right now!")
                                    admin_menu()
                            else:
                                customer_menu()
                        else:
                            print("sorry,you cant login")
                            all_loggers.warning("something is wrong ")

                    else:
                        print("please register")
                        all_loggers.warning("login without register is not true!!")

                except ArithmeticError:
                    print('invalid input,enter your choice.\n')
                    all_loggers.error("Exception occured, user enter invalid input", exc_info=True)
                except ValueError:
                    print('invalid input,enter "A" or "B".\n')
                    all_loggers.error("Exception occured, user enter invalid input in menu", exc_info=True)
                except TypeError:
                    print("enter suitable input")
                    all_loggers.error("Exception occured, user enter invalid input", exc_info=True)


def admin_menu():
    while True:

        # ---------------------admin menu ----------------------
        try:
            admin_choice = input("""
                                                  A: Create new product
                                                  B: Show all products
                                                  C: Show all Factors         
                                                  D: Change user status
                                                  E: Change password
                                                  Q: Logout
    
                                                  Please enter your choice number: """)
        except ArithmeticError:
            print('invalid input,enter your choice.\n')
            all_loggers.error("Exception occured, user enter invalid input", exc_info=True)
        except ValueError:
            print('invalid input,enter "A" or "B".\n')
            all_loggers.error("Exception occured, user enter invalid input in menu", exc_info=True)
        except TypeError:
            print("enter suitable input")
            all_loggers.error("Exception occured, user enter invalid input", exc_info=True)

        else:
            if admin_choice == "a" or admin_choice == "A":

                print("please split items with | ")
                try:
                    name, brand, barcode, price, amount = list(
                        map(lambda x: x.strip(), input("enter name, brand, barcode, price and amount ").split("|")))
                except ValueError:
                    print('invalid input,enter true input.\n')
                    all_loggers.error("product wasnt create")
                else:
                    Admin.create_product(name, brand, barcode, price, amount)
            elif admin_choice == "b" or admin_choice == "B":
                Admin.check_inventory()
            elif admin_choice == "c" or admin_choice == "C":
                Admin.see_all_factor()
            elif admin_choice == "d" or admin_choice == "D":
                user_choice = input("which user do you want to get out of block?\n please, select the name")
                Admin.activate_user(user_choice)
            elif admin_choice == "e" or admin_choice == "E":
                username = input("please enter your username: ")
                old_password = input("enter your old password")
                new_password = input("what is new password:")
                User.change_password(username, new_password, old_password)
            elif admin_choice == "Q" or admin_choice == "q":
                break  # if use exit, system finished all program


def customer_menu():
    # ---------------customer menu ----------------------
    while True:
        try:
            customer_choice = input("""
                                      A: Show all products
                                      B: Buy new product
                                      C: Final factor
                                      D: Change password
                                      Q: Logout

                                      Please enter your choice: """)
        except ArithmeticError:
            print('invalid input,enter your choice.\n')
            all_loggers.error("Exception occured, user enter invalid input", exc_info=True)
        except ValueError:
            print('invalid input,enter "A" or "B".\n')
            all_loggers.error("Exception occured, user enter invalid input in menu", exc_info=True)
        except TypeError:
            print("enter suitable input")
            all_loggers.error("Exception occured, user enter invalid input", exc_info=True)

        else:
            if customer_choice == "a" or customer_choice == "A":
                Products.show_products()
            elif customer_choice == "b" or customer_choice == "B":
                # ------------select the product from list of products name---------

                pd_products = pd.read_csv('Products.csv')
                products_names = list(pd_products['name'])
                print(products_names)
                for product in range(len(products_names)):
                    """
                    customer can buy anything he/she want
                    """
                    try:
                        user_choice = input("what do you want to buy?")
                        customer_amount = int(input(f"how many {user_choice} do you want"))

                        kala = Customer.buy(user_choice, customer_amount)
                        ques = input("do you want to conteniue?")
                        if ques == "NO" or ques == "no" or ques == "No":
                            break
                        elif ques == "yes" or ques == "Yes" or ques == "YES":
                            continue

                        if kala == True:
                            print("congratulation, you buy it successfully ")
                        elif kala == False:
                            print("sorry, try again")


                    except ArithmeticError:
                        print('invalid input,enter currect input.\n')
                        all_loggers.error("Exception occured, user enter invalid input", exc_info=True)
                    except ValueError:
                        print('invalid input,enter a number.\n')
                        all_loggers.error("Exception occured, user enter invalid input", exc_info=True)
                    except TypeError:
                        print("enter suitable input")
                        all_loggers.error("TypeError", exc_info=True)

            elif customer_choice == "c" or customer_choice == "C":
                Customer.see_factor()
            elif customer_choice == "d" or customer_choice == "D":
                try:
                    username = input("please enter your username: ")
                    old_password = input("enter your old password")
                    new_password = input("what is new password:")
                    User.change_password(username, old_password, new_password)
                except ArithmeticError:
                    print('invalid input,enter your username.\n')
                except ValueError:
                    print('invalid input,enter a number.\n')
                except TypeError:
                    print("enter suitable input")

            elif customer_choice == "Q" or customer_choice == "q":
                break

