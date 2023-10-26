def encoder(password):
    new_string = ""
    for i in password:
        if int(i) + 3 > 10:
            new_string += str((int(i) + 3) % 10)
        else:
            new_string += str(int(i) + 3)
    return new_string
if __name__ == "__main__":
    print(encoder("00009962"))
    print(decoder("33332295"))
