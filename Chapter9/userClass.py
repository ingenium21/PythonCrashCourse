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


user1 = User("Renato", "Regalado", "renrega@contoso.com","renato.regalado")

user1.describe_user()
user1.greet_user()
print(user1.loginAttempts)
user1.increment_login_attempts(3)
print(user1.loginAttempts)
user1.reset_login_attemps()
print(user1.loginAttempts)
