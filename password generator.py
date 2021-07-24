import random

print('Welcome to the password generator!')

# we are going to pick random characters from chars string

chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789,./;][!@#$%^&*()"`~{}:'

number = input('Amount of passwords generated: ')  #how many passwords are going to be generated
number = int(number)

#print('\n')
lenght = input('Input the password lenght: ')
lenght = int(lenght)

#print('\n')
print('Here are the passwords: ')

for passw in range(number):
    password = ''
    for c in range(lenght):
        password += random.choice(chars)
    print(password)
