def encoder(password):
    new_string = ""
    for i in password:
        if int(i) + 3 > 10:
            new_string += str((int(i) + 3) % 10)
        else:
            new_string += str(int(i) + 3)
    return new_string

#Alan Skrypek
def decoder(x):
    old_pass = ""
    for i in x:
        if int(i) - 3 < 0:
            old_pass += str((int(i) - 3) % 10)
        else:
            old_pass += str(int(i) -3)
    return old_pass
if __name__ == "__main__":
    password = "123456"
    while True:
        print("Menu")
        print("----------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        opt = input("Please enter an option: ")
        if int(opt) == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            print()
        elif int(opt) == 2:
            print(f"The encoded password is {encoder(password)}, and the original password is {decoder(encoder(password))}.")
            print()
        else:
            break
