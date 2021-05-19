import pandas as pd
import csv
from user import *

user_order_list = []


class Customer(User):

    def __init__(self, username, password):
        super().__init__(self, username, password)

    @staticmethod
    def buy(user_choice,customer_amount ):

        file_path = 'Products.csv'

        pd_products = pd.read_csv(file_path)
        pd_orders = pd.read_csv('user_order.csv')
        products_names = list(pd_products['name'])
        print(products_names)
        count = 0
        while True:

            # user_choice = input("what do you want to buy?")
            # check the product is exist
            if user_choice in products_names:
                # customer_amount = int(input(f'how many {user_choice} do you need?'))
                try:
                    with open('Products.csv', 'r') as product_file:
                        with open('user_order.csv', 'a') as order_file:
                            orders = csv.writer(order_file)
                            products = csv.reader(product_file)

                            count = 0
                            for product in products:

                                if product[0] == user_choice:
                                    # print(product[0])
                                    # ------update the amount of product csv file-----------
                                    product[4] = int(product[4])
                                    if product[4] == 0:
                                        print("Sorry,we dont have it already")
                                        return False
                                    else:
                                        if customer_amount <= int(product[4]):
                                            user_order_list.append(product)
                                            product[4] -= customer_amount
                                            pd_products.loc[count - 1, 'amount'] = product[4]
                                            pd_products.to_csv('Products.csv', index=False)
                                            pd_orders.to_csv('user_order.csv')
                                            user_order = [[product[0], product[3], customer_amount]]
                                            orders.writerows(user_order)

                                            #---------- log new buying for new factors --------------
                                            all_loggers.info(f"{user_choice} was sold.")
                                            return True



                                count += 1

                except:
                    print("File error  ")
            else:

                return False

    @staticmethod
    def see_factor():
        """
        calculate total number of products price
        :return:
        """
        print(user_order_list)
        sum = 0
        for product in user_order_list:
            price = int(product[3]) * int(product[4])
            sum += price
        print("total price :", sum)



