#creating a class queue
class Queue:
    #defining the constructor with a list
    def __init__(self):
        self.items = []
 
    #checking if empty
    def is_empty(self):
        return self.items == []

    #returning the first element
    def front(self):
        return self.items[0]
 
    #adding element
    def enqueue(self, data):
        self.items.append(data)

    #deleting element from front of queue
    def dequeue(self):
        return self.items.pop(0)
 
#creating queue object 
q = Queue()

#looping until true
while True:

    #displaying all options
    print('enqueue <value>')
    print('dequeue')
    print('front')
    print('quit')

    #user prompt for input
    do = input('What would you like to do? ').split()
 
    #converting user input to lowercase
    operation = do[0].strip().lower()

    #checking if operation matches enqueue
    if operation == 'enqueue':
        #extracting the second character string ,converting to int and calling enqueue()
        q.enqueue(int(do[1]))

    #checking if operation matches dequeue
    elif operation == 'dequeue':
        #checking if empty
        if q.is_empty():
            print('Queue is empty.')
            
        else:
            #printing the deleted element
            print('Dequeued value: ', q.dequeue())

    #checking if operation matches front
    elif operation == 'front':
         #checking if empty
        if q.is_empty():
            print('Queue is empty.')
        else:
            #printing the front element
            print('Element at the front of queue is: ',q.front())
    
    #checking if operation matches quit
    elif operation == 'quit':
        #breaks from the while loop
        break