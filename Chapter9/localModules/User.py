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

