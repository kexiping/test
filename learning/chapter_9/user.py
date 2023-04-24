class User:
    """表示用户的简单类"""
    
    def __init__(self, first_name, last_name, username, email, location):
        """初始化用户信息"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0
    
    def describe_user(self):
        """打印用户信息摘要"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
    
    def greet_user(self):
        """问候用户"""
        msg = f"welcome back,{self.username}"
        print(msg)
        
    def increment_login_attempts(self):
        """将属性login_attempts的值加1"""
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """将login_attempts重置为0"""
        self.login_attempts = 0

eric = User('eric', 'matthes', 'e_natthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print(f"Login attempts: {eric.login_attempts}")

print("Restting login attempts...")
eric.reset_login_attempts()
print(f"Login attempts: {eric.login_attempts}")

# willie = User('willies', 'burger', 'willieburger', 'wb@example.com', 'alaska')
# willie.describe_user()
# willie.greet_user()  