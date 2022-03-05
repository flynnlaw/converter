

def DenarytoBinary(denvalue):
    # subroutine to convert decimal into binary
    while True:
        try:
            dec = denvalue
            print("denvalue is" + denvalue)
            dec = dec.strip()
            print(dec)
            break
        except ValueError:
            print("Invalid input, try again")
            break
    while True:
        try:
            while int(dec) > 255 or int(dec) < 0:
                print("Invalid input, try again")
            break
        except ValueError:
            print("Invalid input, try again")
            break
            

# asks for number

    print("The denary value of", dec, "is:")
    frontbit = bin(int(dec))[2:]  # taking off the 0b prefix of the conversion
    while len(
            frontbit
    ) < 8:  #checks the front bit so if lower than 8 it will add one 0 bit to the front to ensure that it is 8 bit
        frontbit = "0" + frontbit
    print(frontbit, "in binary.") #converts the denary to binary
    return frontbit


print(DenarytoBinary("   16"))