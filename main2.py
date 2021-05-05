from userAccount import *


def menu():
    print("************ Welcome to store accounting menu **************")
    print()

    choice = input("""
                      A: Please Register
                      B: Login
                      Q: Logout

                      Please enter your choice: """)

    if choice == "A" or choice == "a":
        User.register()
        menu()
    elif choice == "B" or choice == "b":
        """
        why i cant use User.login() lonely?!!! :(
        """
        User.login = classmethod(User.login)
        User.login()
        """
        Now, depend on the user is admin or customer , the menu fields change
        
        how can call self.user_security_key from register function of admin class????
        
        """
        a = Admin()
        a.register()
        # if a.__class__.__user_security_key__== None:

        # ---------------------admin menu ----------------------
        admin_choice = input("""
                                      A: Create new product
                                      B: See all products
                                      C: See all Factors             #چجوری آخه ؟؟؟؟؟؟؟؟؟
                                      D: Change password
                                      Q: Logout
        
                                      Please enter your choice: """)
        if admin_choice == "a" or admin_choice == "A":
            Admin.create_product()
        elif admin_choice == "b" or admin_choice == "B":
            Admin.check_product_exist()
        elif admin_choice == "c" or admin_choice == "C":
            pass
        elif admin_choice == "d" or admin_choice == "D":
            Admin.change_password()
        elif choice == "Q" or choice == "q":
            exit()

        # elif a.__class__.__user_security_key__== None:
        # ---------------customer menu ----------------------

        customer_choice = input("""
                                      A: See all products
                                      B: Buy new product
                                      C: Final factor
                                      D: Change password
                                      Q: Logout
        
                                      Please enter your choice: """)
        if customer_choice == "a" or customer_choice == "A":
            Products.show_products()
        elif customer_choice == "b" or customer_choice == "B":
            Customer.buy()
        elif customer_choice == "c" or customer_choice == "C":
            Customer.see_factor()
        elif customer_choice == "d" or customer_choice == "D":
            Customer.change_password()
        elif choice == "Q" or choice == "q":
            exit()

    # -----------main menu----------------------
    elif choice == "Q" or choice == "q":
        exit()
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()


if __name__ == '__main__':
    menu()
