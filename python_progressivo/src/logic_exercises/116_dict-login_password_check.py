users_data = {'Clovis': 'whiskas',
              'Nicolas': 'chicken',
              'Ryuk': 'ham'}

user = input("Insert username:")
password = input("Password")

if users_data[user] == password:
    print("Log in sucessfully")
else:
    print("Incorrect data")
