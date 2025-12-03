class Profile:
    def __init__(self,name,email,language):
        self.name=name
        self.email=email
        self.language=language

user1= Profile("Deema","dema@gmail.com","English")
print(f"Welcome to you {user1.name}")
print("\n*******************************************\n")
class User:
    def __init__(self,first_name,last_name,email,password,status="inactive"):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.status=status

def create_user():# ميثود لانشاء الاوبجكت من خلال القيم المدخلة من المستخدم
    first_name=input("Enter your first name : ")
    last_name=input("Enter your last name : ")
    email=input("Enter your email : ")
    password=input("Enter your password : ")
    return User(first_name,last_name,email,password)

user_1=create_user() # انشاء اوبجكت من خلال الميثود السابقة
print(user_1.first_name)