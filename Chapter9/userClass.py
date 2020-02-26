class User:
    def __init__(self, firstName, lastName, emailAddress, username):
        self.firstName = firstName
        self.lastName = lastName
        self.emailAddress = emailAddress
        self.username = username
        self.loginAttempts = 0

    def describe_user(self):
        print(f"First Name: {self.firstName}")
        print(f"Last Name: {self.lastName}")
        print(f"Email Address: {self.emailAddress}")
        print(f"username: {self.username}")
    
    def greet_user(self):
        print(f"Hello {self.firstName.title()}!")

    def increment_login_attempts(self, increment):
        self.loginAttempts += increment
    
    def reset_login_attemps(self):
        self.loginAttempts = 0

class Privileges:
    # a simple class of privileges
    def __init__(self):
        self.privileges = ['can add post',\
                            'can delete post',\
                            'can ban user',\
                            'can add user']
    
    def show_privileges(self):
        print(f"The User has the following privileges: ")
        for i in self.privileges:
            print(i)


class Admin(User):
    #child class for a specific type of user
    def __init__(self, firstName, lastName, emailAddress, username):
        super().__init__(firstName, lastName, emailAddress, username)
        self.privileges = Privileges()


#driver code   
user1 = User("Renato", "Regalado", "renrega@contoso.com","renato.regalado")

user1.describe_user()
user1.greet_user()
print(user1.loginAttempts)
user1.increment_login_attempts(3)
print(user1.loginAttempts)
user1.reset_login_attemps()
print(user1.loginAttempts)

user1Admin = Admin("Renato", "Regalado", "renrega@contoso.com", "renato.adm")

user1Admin.describe_user()
user1Admin.privileges.show_privileges()

