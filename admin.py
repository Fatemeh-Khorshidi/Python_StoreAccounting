import pandas as pd
import csv

from Product import Products
from user import *

admin_identity = []


class Admin(User):

    def __init__(self, username, password, status):
        super().__init__( username, password, status)

    # ---------the admin has security key as extra input------------

    @staticmethod
    def create_product(name, brand, barcode, price, amount):
        """
        this function get kala from admin
        :return:
        """

        # name, brand, barcode, price, amount = input("enter name, brand, barcode, price and amount ").split("|")
        kala = Products(name, brand, barcode, int(price), int(amount))
        print("product created")
        all_loggers.info(f"new product created by name {kala.name}")

        # ---------Add products to csv file that named by product csv -----------

        file_path = "Products.csv"
        df_account = pd.read_csv(file_path)

        row_account = [[kala.name, kala.brand, kala.barcode, kala.price, kala.amount]]
        try:
            with open(file_path, 'a', newline='')as product_file:
                csv_writer = csv.writer(product_file)
                csv_writer.writerows(row_account)
        except:
            print("File error  ")

        return kala
    # class product.create_product
    @staticmethod
    def check_inventory():
        """
            the user should know the number of products
            تابع# چک موجودی انبار
        """
        file_path = 'Products.csv'
        product_file = pd.read_csv(file_path)
        print(product_file)

    @staticmethod
    def activate_user(user_choice):
        file_path = 'account.csv'
        read_file = pd.read_csv(file_path)
        # print(false)
        count = 0
        count_number = 0  # just for insert number next to the names
        # ---------first: show the usernames that theyr status is false ----------------
        for row in read_file.itertuples():
            if row.status == False:
                print(f" {count_number}: {row.username}")
                count_number += 1
            else:
                print("no one is block")
                continue
        try:
             with open(file_path, 'r') as csvfile:
                datareader = csv.reader(csvfile)
                # user_choice = input("which user do you want to get out of block?\n please, select the name")
                for user in datareader:
                    if user[0] == user_choice:
                        # !-----------------update password in file -----------------!
                        print(f"{user_choice} is active successfully")
                        read_file.loc[count - 1, 'status'] = 'True'
                        read_file.to_csv('account.csv', index=False)
                    count += 1
        except:
            print("File error  ")
    @staticmethod
    def see_all_factor():
        """
        calculate total number of products price
        :return:
        """
        try:
            with open('user_order.csv', 'r') as userorder_file:
                read_file = csv.reader(userorder_file)
                count = 0
                sum = 0
                for product in read_file:
                    if count == 0:
                        count += 1
                    else:
                        price = int(product[3]) * int(product[4])
                        sum += price

                        count += 1
        except:
            print("File error  ")
        # print("total price :", sum)
        print(f"{product[4]} number of {product[0]}, total price: {sum}")
