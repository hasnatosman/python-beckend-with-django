print('Create an account!')

user_name = input('Input your name: ')
user_password = input('Input a password: ')

print('Account created succesfully!')

print('..........Log in now....................')

user_name2 = input('Give you user name : ')
user_password2 = input('Give your password : ')

if user_name == user_name2:
    if user_password == user_password2:
        print('Successfully Logged In!')
    else:
        print('Password is not correct!')
        print('Try again!!')
else:
    print('User name didnot matched!')
    print('Try again!!')