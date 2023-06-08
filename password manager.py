master_pwd = input("what is the master password?")

def view():
    with open("passwords.txt", "a")  as f:
        for line in f.readline():
            print(line.rstrip())

def add():
    name = input("account name : ")
    pwd = input("Password: ")

    with open("passwords.txt", "a")  as f:
        f.write(name + ":" + pwd + "\n" )
while True:
    mode = input("would you like to add a new password or existing ones (view ,add,Q )")
    if mode == "Q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode.")
        continue