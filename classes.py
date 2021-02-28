class User:
    def __init__(self, name, age, password, email):
        self.__name = name
        self.__age = age
        self.__email = email
        self.__password = password

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    email = property(get_email, set_email)

class ExendUser(User):
    def __init__(self, name, age, password, email):
        super(ExendUser, self).__init__(name, age, password, email)



user1 = User("Vasya", 20, "123", "vasya@gmail.ru")
user2 = User("Petya", 23, "1324", "petya@gmail.ru")

print(user1)
print(user2)



