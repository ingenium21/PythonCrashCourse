from localModules.User import User
from localModules.admin import Privileges,Admin

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

