class User:
    login_attempts = 0

    def __init__(self):
        pass # pass means do nothing, it is just place holder
        ### self.login_attempts = 0 this is the alternative way of creating global variable
    def increment_login_attempt(self):
        print("incrementing the value by 1 ...")
        self.login_attempts += 1

    def reset_login_attempt(self):
        print("reseting the value to 0 ...")
        self.login_attempts = 0

user1 = User()
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()
print("Login attempts: ", user1.login_attempts)
user1.reset_login_attempt()
print("Login attempts: ", user1.login_attempts)
