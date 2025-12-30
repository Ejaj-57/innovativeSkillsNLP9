login_password_db = '123456'

user_input_password = input('Enter your password: ')

if user_input_password == login_password_db:
    print('Login successful')
else:
    print('Login failed')