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
    print(encoder("00009962"))
    print(decoder("33332295"))
