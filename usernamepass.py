cor_username="Admin"
cor_password="admin123"
username = input("enter the username: ")
password = input("enter the password: ")
if username==cor_username and password==cor_password:
    print('login sucessful ')
elif username!= cor_username:
    print('username not found')
elif password!=cor_password:
    print('password incorrect')
    