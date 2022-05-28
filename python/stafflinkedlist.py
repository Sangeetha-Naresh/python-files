#creating the node class with attributes in the constructor dataval an nextval
class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None

#creating the class staff with attributes head and tail defines in the constructor
class Staff:
    def __init__(self):
        self.head = None
        self.tail = None

    # change method given in the question that reverse the list
    def change(self):
        self.tail = self.head 
        temp = self.head.nextval
        while(temp!=None):
            A=temp.nextval
            temp.nextval=self.head
            self.head=temp
            temp=A
        self.tail.nextval=None

    # function to insert a Node at required position
    def insertPos(self,position,data):
         
        headNode=self.head
        # This condition to check whether the
        # position given is valid or not.
        if position < 1:       
            print("Invalid position!")
        
        if (position == 1):
            newNode = Node(data)
            newNode.nextval = headNode
            headNode = newNode

        else:
        
            # Keep looping until the position is zero
            while (position != 0):          
                position -= 1

                if (position == 1):
  
                    # adding Node at required position
                    newNode = Node(data)
        
                    # Making the new Node to point to
                    # the old Node at the same position
                    newNode.nextval = headNode.nextval
        
                    # Replacing headNode with new Node
                    # to the old Node to point to the new Node
                    headNode.nextval = newNode
                    break
             
                headNode= headNode.nextval
                if (headNode == None):
                    break
   
 # Print the list
    def listprint(self):
        printval = self.head
        #print(printval)
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

#creating list as the staff object
list = Staff()

#creating the node Ali and asigning it as the head of staff list
list.head = Node("Ali")

#creating the node objects Abu, Man, Dol
e2 = Node("Abu")
e3 = Node("Man")
e4 = Node('Dol')

#assigning the node e2("Abu") as the next value of the head node
list.head.nextval = e2

#assigning the node e3("Man") as the next value of the node e2
e2.nextval = e3

#assigning the node e4("Dol") as the next value of the node e3
e3.nextval = e4

print("Printing the staff list before calling the change method: ")
list.listprint()

#calling the change method
list.change()


print("Printing the staff list after calling the change method: ")
list.listprint()

pos=int(input("Enter the position: "))
data=input("Enter data: ")

list.insertPos(pos,data)

print("Linked list after insertion at the specified position")
print("")
list.listprint()

