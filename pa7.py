### CheckLen Function ###
def CheckLen (num):
    if len(num) >= 13 and len(num) <= 16:
        return True
    else:
        return False

### DetermineType Function ###
def DetermineType (num):
    if num[0] == '4':
        return 'Visa'
    elif num[0] == '5':
        return 'MasterCard'
    elif num[0:2] == '37':
        return 'American Express'
    elif num[6] == '6':
        return 'Discover'

### algorithmDigitSum ###
def algorithmDigitSum(num):
    sumDouble = 0
    for i in range (len(num)-1-1, 0-1, -2):
        digit = eval(num[i])
        double = 2 * digit
        if double > 9:
            d1 = eval(str(double)[0])
            d2 = eval(str(double)[1])
            double = d1+d2
        sumDouble += double
    
    sumOdd = 0
    for i in range (len(num)-1-2, 0-2, -2):
        digit = eval(num[i])
        sumOdd +=  digit
    
    totalSum = sumDouble + sumOdd
    if totalSum % 10 == 0:
        return True
    else:
        return False

### VerifyValid Composite Function ###
def verifyValid(num):
    if CheckLen(num) and algorithmDigitSum(num):
        print("Valid", end = '               ')
        print(DetermineType(num))
    else:
        print("Invalid")

### printHeader Function ###
def printHeader():
    print("Number                   Valid/Invalid       Type")
    print("-----------------------------------------------------")

### main Function ###
def main():
    printHeader()
      
    inFile = open("pa7.cards","r")
    cardNumber = inFile.readline().strip()
    while cardNumber != '99999':
        print(format(cardNumber, '16s'), end = '         ')  
        verifyValid(cardNumber)
        
        cardNumber = inFile.readline().strip()
    
    inFile.close()
main()