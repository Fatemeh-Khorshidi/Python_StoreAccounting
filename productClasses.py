"""
initial class for things and materials
مدیر فروشگاه اجناس را تعریف میکند: برای هر جنس بارکد، قیمت، برند، نام کالا و تعداد موجودی آن را
مشخص میکند.
"""


class Products:
    def __init__(self, barcode, price, brand, name, amount):
        self.barcode = barcode
        self.price = price
        self.brand = brand
        self.name = name
        self.amount = amount

    @staticmethod
    def creat_product():
        """
        this function get kala from admin
        :return:
        """
        barcode, price, brand, name, amount = input("enter them").split("|")
        kala = Products(barcode, int(price), brand, name, int(amount))
        return kala

    def add_to_file(self):
        """
        create a svg file and save the items in it
        :return:
        """
        with open("Products.csv", 'x') as Products_info:
            Products_info.write("user infos")



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

# Products.add_to_file = classmethod(Products.add_to_file )
# Products.add_to_file()