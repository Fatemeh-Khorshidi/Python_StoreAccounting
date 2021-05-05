import pandas as pd


class Products:
    """
    initial class for things and materials
    مدیر فروشگاه اجناس را تعریف میکند: برای هر جنس بارکد، قیمت، برند، نام کالا و تعداد موجودی آن را
    مشخص میکند.
    """

    def __init__(self, barcode, price, brand, name, amount):
        self.barcode = barcode
        self.price = price
        self.brand = brand
        self.name = name
        self.amount = amount

    def show_products(self):
        file_path = 'Products.csv'
        """
        read specific columns (brand,name,price) of csv file using Pandas
        """
        all_products = pd.read_csv(file_path, usecols=['brand', 'name', 'price'])
        print(all_products)

    """
    Alert the zero number of products
    """

    def __str__(self):
        """
        Is the customer able to observe the products or need a new function by the str function ?

        :return:
        """
        print({self.name}, {self.brand}, {self.price})

# num = int(input("numbers"))
#
# list=[]
# for i in range (num):
#     a = Products.get_kala()
#     list.append(a)
#
# print(list)

# Products.show_products = classmethod(Products.show_products )
# Products.show_products()
