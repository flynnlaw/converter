import math
#all subroutines (Except for the first 3 below) are taken from https://replit.com/@ZachLines/Converter#main.py (collab)
#above repl is the master cli interface that was complied in a few weeks and works on its own
#all below subroutines have been either made specifically or modified to work with the code in main.py and have returned values
#------------------------------------------------------------------------------------------------
def BinaryToBinary(lol):
    return("You can't convert Binary to itself")

def DenaryToDenary(lol):
    return("You can't convert Denary to itself")

def HexToHex(lol):
    return("You can't convert Hexadecimal to itself")


def DenaryToBinary(denvalue):
    # subroutine to convert decimal into binary
    while True:
        try:
            dec = denvalue
            dec = dec.replace(" ", "")#deletes all spaces from the input
            dec = dec.split(" ")
            dec = dec[0]
            dec = dec.replace("\n", "")
            break
        except ValueError:
            return("Invalid input, try again")
    while True:
        try:
            while int(dec) > 255 or int(dec) < 0: #checks input is within the range and format we want to accept
                return("Invalid input, try again")
            break
        except ValueError:
            return("Invalid input, try again")
            

# asks for number

   
    frontbit = bin(int(dec))[2:]  # taking off the 0b prefix of the conversion
    while len(
            frontbit
    ) < 8:  #checks the front bit so if lower than 8 it will add one 0 bit to the front to ensure that it is 8 bit
        frontbit = "0" + frontbit
  #converts the denary to binary
    return frontbit



#-----------------------------------------------------------------------------------------------------


def BinaryToDenary(binvalue):
    while True:
        binary = binvalue
        binary = binary.replace(" ", "")
        binary = binary.split(" ")
        binary = binary[0]
        binary = binary.replace("\n", "")
        print(binary)
        if len(binary) == 0:
            break

        if len(binary) != 8:  #checks that it has a length of 8 binary digits
            return("Invalid input, 8 bits required!")

        split_strings = []
        n = 2
        for index in range(0, len(binary), n):
            split_strings.append(binary[index:index + n])

        for item in split_strings:  #checks that all chracters inputted are in binary 0s and 1s
            if item not in {'00', '01', '10', '11'}:
                return("Invalid input, try again !")
                break  #used to allow escape out of for loop if statement triggered
        
        else:
            binvalue = (int(binary, 2)) #converts it into denary
            return binvalue
            #    print(int(binary,2))  #converts it into denary
    
    return("Invalid input, try again")

#----------------------------------------------------------------------------------------------------------


def BinaryToHex(binvalue):

    conversion_table = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
        'E', 'F'
    ]

    while True:
        binary = binvalue
        binary = binary.replace(" ", "")
        binary = binary.split(" ")
        binary = binary[0]
        binary = binary.replace("\n", "")

        for item in binary:  #checks that all chracters inputted are in binary 0s and 1s
            if item not in {'0', '1'}:
                return("Invalid input, try again !")

                #used to allow escape out of for loop if statement triggered

        if len(binary) != 8:  #checks that it has a length of 8 binary digits
            return("Invalid input, 8 bits required!")


        else:
            abc = (int(binary, 2))
            hexadecimal = conversion_table[math.ceil((abc / 16) - 1)]
        while (abc > 0):
            remainder = abc % 16
            hexadecimal = hexadecimal + conversion_table[remainder]
            abc = abc // 16
            while len(hexadecimal) < 2:
                hexadecimal = "0" + hexadecimal

            return hexadecimal
            break



#--------------------------------------------------------------------------------------------------


def DenaryToHex(denvalue):

    conversion_table = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
        'E', 'F'
    ]

    while True:
        try:
            decimal = denvalue
            decimal = decimal.replace(" ", "")
            decimal = denvalue
            decimal = decimal.replace(" ", "")#deletes all spaces from the input
            decimal = decimal.split(" ")
            decimal = decimal[0]
            decimal = decimal.replace("\n", "")
            break
        except ValueError:
            return("Invalid input, try again")
    while True:
        try:
            if (decimal.isnumeric()) == True:
                abc = int(decimal)
            else:
                while (decimal.isnumeric()) == False:
                    decimal = denvalue
                    decimal = decimal.strip()
                    if (decimal.isnumeric()) == True:
                        abc = int(decimal)
            while int(decimal) > 255 or int(decimal) <= 0:
                return("Invalid input, try again")
                
            break
        except ValueError:
            return("Invalid input, try again")

# asks for number

    hexadecimal = ''

    while (abc > 0):
        remainder = abc % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        abc = abc // 16

    return hexadecimal

   


#---------------------------------------------------------------------------------------------------


def HexToBinary(hexvalue):
    # hexadecimal string
    novalues = readFile("HexValues.txt")
    hexinput = hexvalue  #askin("g for a hex value
    hexinput = hexinput.replace(" ", "")
    hexinput = hexinput.split(" ")
    hexinput = hexinput[0]
    hexinput = hexinput.replace("\n", "")
    hexinput = hexinput.upper()
    
    while len(hexinput) == 1:
        return ("Hex value has to be 2 digits")

    while len(hexinput) != 2 and len(hexinput) > 2:
        return("Invalid input, try again")
       

    while hexinput not in novalues:
        return("Invalid input, try again")
        

    dec = int(hexinput, 16)
    frontbit = bin(int(dec))[2:]  # taking off the 0b prefix of the conversion
    while len(
            frontbit
    ) < 8:  #checks the front bit so if lower than 8 it will add one 0 bit to the front to ensure that it is 8 bit
        frontbit = "0" + frontbit
    return frontbit  #converts the denary to binary

    

#------------------------------------------------------------------------------------------------------


def HexToDenary(hexvalue):
    # hexadecimal string
    novalues = readFile("HexValues.txt")
    hexinput = hexvalue  #asking for a hex value
    hexinput = hexinput.replace(" ", "")
    hexinput = hexinput.split(" ")
    hexinput = hexinput[0]
    hexinput = hexinput.replace("\n", "")
    hexinput = hexinput.upper()
    
    while len(hexinput) == 1:
        return ("Hex value has to be 2 digits")


    while len(hexinput) != 2 and len(hexinput) > 2:
        return("Invalid input, try again")

    while hexinput not in novalues:
        return("Invalid input, try again")

    dec = int(hexinput, 16)
    return dec

def readFile(fileName):
    fileObj = open(fileName, "r")  #opens the file in read mode
    hexarray = fileObj.read().splitlines()  #puts the file into an array
    fileObj.close()
    return hexarray


#----------------------------------------------------------------------------------------------------------------------


def BinaryAddition(binvalue1, binvalue2):
    print(binvalue1, binvalue2)

    while True:
        binary1 = binvalue1
        binary1 = binary1.replace(" ", "")
        binary1 = binary1.split(" ")
        binary1 = binary1[0]
        binary1 = binary1.replace("\n", "")
        print(binary1)
        
        if len(binary1) == 0:
            return("Binary value(s) is/are empty"), 0
        

        for item in binary1:  #checks that all chracters inputted are in binary 0s and 1s
            if item not in {'0', '1'}:
                return 1, 0
                #break  #used to allow escape out of for loop if statement triggered

        if len(binary1) != 8:  #checks that it has a length of 8 binary digits
            return 2, 0

        else:
            break

    while True:
        binary2 = binvalue2
        binary2 = binary2.replace(" ", "")
        binary2 = binary2.split(" ")
        binary2 = binary2[0]
        binary2 = binary2.replace("\n", "")
        
        if len(binary2) == 0:
            return("Binary value(s) is/are empty"), 0

        for item in binary2:  #checks that all chracters inputted are in binary 0s and 1s
            if item not in {'0', '1'}:
                return 3, 0
                break  #used to allow escape out of for loop if statement triggered

        if len(binary2) != 8:  #checks that it has a length of 8 binary digits
            return 4, 0

        else:
            break
    try:
        res = bin(
            int(binary1, 2) +
            int(binary2, 2))  #passing the base value of 2 for binary to the i

    except ValueError:
        return("Invalid input, try again"), 0

#gets rid of the ob suffix and says if overflow error to allow it to be 8 bit total
    frontbit = (res[2:])
    if len(frontbit) > 8:
        frontmorebit = (frontbit[1:])
        
        return(frontmorebit), 1
        
    else:
        return(frontbit), 0


#---------------------------------------------------------------------------------------------------------------------
    


