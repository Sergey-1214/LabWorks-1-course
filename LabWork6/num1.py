class UserAccount:
    def __init__(self,username:str,email:str,password:str):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self,new_password:str):
        self.__password = new_password

    def check_password(self,password:str)->bool:
        if self.__password == password:
            return True
        else:
            return False
user = UserAccount('a','b','c')
user.set_password('password')
print(user.check_password('pass'))
print(user.check_password('password'))