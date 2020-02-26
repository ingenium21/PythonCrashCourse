from localModules.User import User

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

