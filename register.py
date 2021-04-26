class Register:
    """
    the user must inter his/her information on this system.
    note: the information such as fullname and username must be unique
    Its will be funny if write captcha code!

    """
    def __init__(self, Fullname, username, Email, password, repassword ):
        self.Fullname = Fullname
        self.username = username
        self.password = password
        self.repassword = repassword
        self.Email = Email


    def get_info(self):
        """
        get information from user
        check the password is equal to repassword in this function. is that true?
        """
        pass


    def save_in_csv(self):
        with open("register.csv" , 'a') as register_info:
            register_info.write("user infos")

        """
        save the information in svg database
        :return:
        """


    def check_user(self):
        """
        check is the user registered or not and if user registered, tell
        :return: 
        """
        pass

# Register.save_in_csv = classmethod(Register.save_in_csv )
# Register.save_in_csv()