#defining the createUserId method by passing first name, last name and phone number
def createUserId(f, l,p):
    
    #creating an empty list
    userId=[]

    #appending the first character of first name to user id
    userId.append(f[0])

    #appending the first four characters of last name to user id
    userId.append(l[0])
    userId.append(l[1])
    userId.append(l[2])
    userId.append(l[3])

    #finding the length of the string phone number
    n=len(p)

    #appending the last four characters of phone number to user id
    userId.append(p[n-4])  
    userId.append(p[n-3])
    userId.append(p[n-2])
    userId.append(p[n-1])
    
    #printing the user id
    print("Hello ",f," ", l)
    print("your user id is : ", "".join(userId))
   

#defining the method to get the user input
def getUserinput():
    #getting the first name from user input
    f=input("Enter your first name: ")
    
    #getting the last name from user input
    l=input("Enter your last name: ")
  
    #getting the phone number from user input
    p=input("Enter your phone number: ")

    #calling the createUserId method
    createUserId(f, l,p)

def main(): 
    getUserinput()
    

if __name__ == "__main__":
    main()