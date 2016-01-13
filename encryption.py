import random






# Generates and returns a random key
def keyGen(alpha):      
        key = ""
        for i in range(len(alpha)):
            index = random.randint(0, 25-i)
            key = key + alpha[index]
            alpha = alpha[:index] + alpha[index+1:]
        return key
#end of keyGen()






# Encrypts plaintext using a random key and a Caeser cipher
def caes_siph(plainText):
# header for function caesar that takes plainText as an argument
        
        key = keyGen("abcdefghijklmnopqrstuvwxyz")
        print("Random key: ")
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        print(alphabet)
        
        print(key)

        # convert plainText to all lowercase letters
        plainText.lower()


        cipherText = []
        for ch in plainText:
            idx = alphabet.find(ch)
            #_______x________
            # if index is positive
            if idx > -1:
                # append to cipherText a character sitting in key[idx]
                cipherText.append(key[idx])
            
            # else if index is negative but ch is a digit
            elif idx < 0 and ch.isdigit() :
                # append that digit to cipherText
                cipherText.append(ch)

            # else if index is negative but ch is not a digit
            elif idx < 0 and not ch.isdigit() :
                # append a blank to cipherText
                cipherText.append(' ')



        return ''.join(cipherText)
#end of caes_ciph()






# Encrypts plaintext using transposition cipher
def trans(plainText):
        
        #_____________x____________
        # extract all chars sitting in even positions into evenChars string
        evenChars = []
        for index, item in enumerate(plainText):
            if index % 2 == 0 :
                evenChars.append(item)
        
        # extract all chars sitting in odd positions into oddChars string
        oddChars = []
        for index2, item2 in enumerate(plainText) :
            if index2 %2 == 1 :
                oddChars.append(item2)


        cipherText = ''.join(oddChars) + ''.join(evenChars)
        return cipherText
#end of trans()







# Encrypts plaintext using ASCII shift
def ascii_shift(plainText):
        shift = random.randint(1, 25)
        print("Shift: ", shift)


        # _____________
        # construct and return cipherText as plainText in which 
        # each char is replaced with old char + shift (look up chr and ord functions)
        cipherText = ""


#end of ascii_shift()







# Driver
def my_main():

    # _____________x______________
    # prompt for a phrase, store results into variable msg
    msg = input('Enter a message to encrypt: ')
    
    
    print('Which encryption do you want to use?')
    choice = input('Enter 1 for random Caeser cipher, 2 for transposition, 3 for an ASCII shift: ')
    if choice.isdigit() :
        int_choice = int(choice)
        
        
        # ______________x_____________
        # while statement that is entered if choice contains more than just digits
        # or int_choice is not within the range [1, 3]
        if int_choice not in [1,2,3] :
            print('Invalid input - try again')
            choice = input('Enter 1 for random Caeser cipher, 2 for transposition, 3 for an ASCII shift: ')
            if choice.isdigit():
                int_choice = int(choice)


    # _________x______________
    # based on the user's choice (1, 2 or 3)  call appropriate encryption function and
    # store the result into variable cipherText
    if int_choice == 1 :
        cipherText = caes_siph(msg)
    elif int_choice == 2 :
        cipherText = trans(msg)
    elif int_choice == 3 :
        cipherText = ascii_shift(msg)


    print('The encrypted message is: ', cipherText)





if __name__ == '__main__':
        my_main()

        
    
    


