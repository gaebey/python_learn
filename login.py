username = input("username: ")
password = input("password: ")

if username.lower() == "admin" and password.lower() == "secret123":
    print("Access Granted!")
else:
    print("Access Denied... loser.")
