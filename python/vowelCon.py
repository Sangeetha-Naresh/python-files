#defining the VowelCount method by passing string
def VowelCount(str):

    #initializing vowels to 0
    vowels=0

    #looping through the string
    for i in str:
        #checking if vowel both in upper and lower cases
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            #incrementing the vowel count by 1
            vowels=vowels+1

    #returning the number of vowels
    return vowels

#defining the ConsonantCount method by passing string
def ConsonantCount(str):
  #initializing consonants to 0
    consonants=0
    
    #looping through the string
    for i in str:
         #checking if NOT vowel both in upper and lower cases and also spaces
        if(i!='a' and i!='e' and i!='i' and i!='o'and i!='u' and i!='A' and i!='E' and i!='I' and i!='O' and i!='U'and i!=' '):
         #incrementing the consonant count by 1
            consonants=consonants+1
    return consonants

#defining the method to get the user input
def getUserString():

    #getting the string from user input
    str=input("Enter a string: ")
    
    #calling the VowelCount method
    v=VowelCount(str)

    #calling the VowelCount method
    c=ConsonantCount(str)

    #printing the vowel count and consonant count
    print("Number of vowels are: ",v," and the number of consonants are: ", c)



def main(): 

    #calling the getUserString method
    getUserString()
    
#calling the main()
if __name__ == "__main__":
    main()