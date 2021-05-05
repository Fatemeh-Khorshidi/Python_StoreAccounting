import pandas as pd
import csv
import hashlib
from tempfile import NamedTemporaryFile

from productClasses import Products


class User:
    """
        the user must inter his/her information on this system.
        note: the information such as fullname and username must be unique
        Its will be funny if write captcha code!

        """

    def __init__(self, username, password, repassword, hash_password=None):

        self.password = password
        self.username = username
        self.repassword = repassword
        self.hash_password = hash_password

    #         چحوری تشخیص دهیم کاربر ادمینه یا مشتری

    # -----------------Register----------------
    @staticmethod
    def register():
        file_path = "account.csv"
        df_account = pd.read_csv(file_path)
        list_username = list(df_account['username'])

        # ------------check the username exist-----------
        while True:
            username = input("Enter username:")
            if username in list_username:
                print("username is exist")
            else:
                break

        # security_key = input("if you are admin inter security_key ")
        password = input("Enter password:")
        while True:
            repassword = input("Enter password again:")
            if repassword != password:
                print("The invalid password")
            else:
                break
                # elif repassword!=password:

        hash_password = hashlib.sha256(password.encode('utf8')).hexdigest()

        # -----------save to svg file--------------
        user = User(username, password, repassword, hash_password)
        row_account = [[user.username, user.password, user.hash_password]]

        with open(file_path, 'a', newline='')as scv_file:
            csv_writer = csv.writer(scv_file)
            # writing the data row
            csv_writer.writerows(row_account)

        return user

    def login(self):
        """

        :return:
        """

        file_path = "account.csv"
        df_account = pd.read_csv(file_path)
        list_username = list(df_account['username'])

        username = input("enter username")

        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            count = 0
            login_count = 0
            if username in list_username:
                for row in csv_reader:
                    if count == 0:
                        count += 1

                    else:
                        while login_count < 3:  # user cant inter incorrect password more than 3 times

                            new_password = input("Enter password: ")
                            hash_password = hashlib.sha256(new_password.encode('utf8')).hexdigest()
                            print(hash_password)
                            print(row[2])
                            """
                            why dont loop ??? :(
                            """

                            if hash_password == row[2]:

                                self.username = username
                                self.password = new_password
                                self.hash_password = hash_password
                                print(f'your login success!!')

                                # there are difference between custmer and admin register so i ask from user...

                                """
                                is it true for override functions???
                                """

                                identify_question = input("Are you Admin?").lower()
                                if identify_question == "yes":
                                    Admin.register()
                                else:
                                    pass
                                break
                            else:
                                print('Access denied. Try again.')
                                login_count += 1
                        count += 1
            else:
                print("please go back to the menu and register...")

    def change_password(self):
        print(self.password)
        tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
        with open('account.csv') as csv_file, tempfile:
            csv_reader = csv.reader(csv_file, delimiter=',')
            csv_writer = csv.writer(tempfile, delimiter=',')

            new_pass = input("what is new password:")
            hash_password = hashlib.sha256(new_pass.encode('utf8')).hexdigest()
            for row in csv_reader:
                if self.username == row[0]:
                    print(row[0])
                    row[1] = row[1].replace(self.hash_password, hash_password)
                    print(row[1])
                    a = csv_writer.writerow(row[1])
                    print(a)
                    """
                    !-----------------unfinished-----------------!
                    """


class Admin(User):

    def __init__(self, username, password, repassword, user_security_key=None):
        super().__init__(self, username, password, repassword)
        self.user_security_key = user_security_key

    # ---------the admin has security key as extra input------------

    def register(self):
        security_key = 1234
        user_security_key = int(input("For identify admin, please enter security key "))
        if security_key == user_security_key:
            self.security_key = user_security_key
            print("welcome admin..")
            """
            Alert the zero number of products
            """

            Admin()
        else:
            Customer()

        return self.security_key

    def create_product(self):
        """
        this function get kala from admin
        :return:
        """
        print("please split items with | ")
        barcode, price, brand, name, amount = input("enter barcode, price, brand, name and amount ").split("|")
        kala = Products(barcode, int(price), brand, name, int(amount))
        # ---------Add products to csv file that named by product csv -----------

        file_path = "Products.csv"
        df_account = pd.read_csv(file_path)

        row_account = [[kala.barcode, kala.price, kala.brand, kala.name, kala.amount]]
        with open(file_path, 'a', newline='')as product_file:
            csv_writer = csv.writer(product_file)
            csv_writer.writerows(row_account)

        return kala

    # class product.create_product

    def check_product_exist(self):
        """
            the user should know the number of products
            تابع# چک موجودی انبار
        """
        file_path = 'Products.csv'
        product_file = pd.read_csv(file_path)
        print(product_file)
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            count = 0
            for product in csv_reader:
                if count == 0:
                    count += 1
                else:
                    print(f'we have {product[4]} number of {product[0]} ')


class Customer(User):
    def __init__(self, username, password, repassword, ):
        super().__init__(self, username, password, repassword)
        pass

    def buy(self):

        file_path = 'Products.csv'

        exist_products = pd.read_csv(file_path)
        names_list = list(exist_products['name'])
        while True:
            user_choice = input("what do you want to buy?")
            # check the product is exist
            if user_choice in names_list:

                no_product = int(input(f'how many {user_choice} do you need?'))
                break
            else:
                print("Sorry, we dont have it.")

        row_info = [[user_choice, no_product]]
        with open('user_order.csv', 'a') as user_file:
            append_file = csv.writer(user_file)

            with open('Products.csv') as product_file:
                # append this product to buy list
                products = csv.reader(product_file)
                update_products = csv.writer(product_file)
                count = 0
                for item in products:
                    if count == 0:
                        count += 1
                    else:
                        if user_choice == item[3]:
                            # check the number of product exist
                            if no_product < int(item[4]):
                                item[4] = no_product
                                append_file.writerow(item)
                                # updating the column value/data

                                # *-*-*-*-*--*-*-*-*-***-**----
                                new_amount = int(item[4]) - no_product

                                text = ''.join([i for i in product_file]).replace(str(item[4]), str(new_amount))
                                print(text)

                                product_file.writelines(text)
                                """
                                 !-----------------unfinished replace in csv file -----------------!
                                 """
                                # *-*-*-*-*--*-*-*-*-***-**--

                            else:
                                print("Sorry, Currently , the stock has been finished .")

                        else:
                            print("Sorry, we dont have it.")

                """
                2- update the number of products --> sum of the bought of them,and sum of the 
                remind of them

                """

    def see_factor(self):
        """
        calculate total number of products price
        :return:
        """
        with open('user_order.csv', 'r') as userorder_file:
            read_file = csv.reader(userorder_file)
            count = 0
            sum = 0
            for product in read_file:
                if count == 0:
                    count += 1
                else:
                    price = int(product[1]) * int(product[4])
                    sum += price

                    count += 1
        print("total price :", sum)

# User.register()
# User.login= classmethod(User.login)
# User.login()
# User.change_password = classmethod(User.change_password)
# User.change_password()
# Admin.check_product_exist = classmethod(Admin.check_product_exist)
# Admin.check_product_exist()
# Customer.see_factor = classmethod(Customer.see_factor)
# Customer.see_factor()
# importing the pandas library
# import pandas as pd  #
# reading the csv file
# df = pd.read_csv("AllDetails.csv")
# updating the column value/data
# df.loc[5, 'Name'] = 'SHIV CHANDRA'
# writing into the file
# df.to_csv("AllDetails.csv", index=False)
# print(df)
