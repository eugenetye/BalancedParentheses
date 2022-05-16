class Stack(object):

    # constuctor for stack class
    def __init__(self):
        self.__linkedList = LinkedList()            
        self.__top = -1                             

    # push item onto stack
    def push(self, x):                                           
        self.__linkedList.add(x)
        self.__top += 1

    # pops item from top of stack
    def pop(self):
        popped_item = self.__linkedList.remove(self.__top)      
        self.__top -= 1
        return popped_item

    #returns Boolean of whether stack is currently empty
    def isEmpty(self):
        if self.__linkedList.get_head() == None:
            return True
        else:
            return False

    # returns Boolean of whether stack is currently full
    def isFull(self):
        if self.__linkedList.__capacity == 0:
            return True
        else:
            return False

    # clears the stack
    def clear(self):
        self.__linkedList = LinkedList()
        self.__top = -1

    # looks at the top of the stack without removing it
    def peek(self):
        head = self.__linkedList.get_head()
        top_value = head.get_data()
        return top_value

class Queue(object):

    # constructor for Queue class
    def __init__(self):
        self.__linkedList = LinkedList()
        self.__front = -1
        self.__rear = -1

    # adds item to front of queue
    def enqueue(self, x):
        self.__linkedList.add(x)
        self.__rear += 1

    # removes item from rear of queue
    def dequeue(self):
        dequeued_item = self.__linkedList.remove(self.__front)
        self.__front += 1
        return dequeued_item

    # returns Boolean of whether queue is currently empty
    def isEmpty(self):
        if self.__linkedList.get_head() == None:
            return True

        else:
            return False

    # returns Boolean of whether queue is currently full
    def isFull(self):
        if self.__linkedList.__capacity == 0:
            return True
        else:
            return False 

    # clears the queue
    def clear(self):
        self.__linkedList = LinkedList()
        self.__front = -1
        self.__rear = -1
    
    # looks at the item at the end of the queue without removing it
    def poll(self):
        tail = self.__linkedList.get_tail()
        end_item = tail.get_data()
        return end_item

class LinkedList(object):

    # constructor for LinkedList class
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__capacity = 0
        self.__size = 0

    # setters and getters
    def set_head(self, head):
        self.__head = head
    
    def get_head(self):
        return self.__head

    def set_tail(self, tail):
        self.__tail = tail
    
    def get_tail(self):
        return self.__tail

    def set_size(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    # add item x to list 
    def add(self, x):
        node = Node()
        node.set_data(x)
        node.set_next(self.__head)
        
        if self.__head == None:
            self.__tail = node
            
        self.__head = node
        self.__size += 1
        return True

    # remove item at index i from the list
    def remove(self, i):
        if i == 0:
            removed_item = self.__head.get_data()
            self.__head = self.__head.get_next()
            if self.__head == None:
                self.__tail = None

        elif i == self.__size - 1:
            removed_item = self.__tail.get_data()
            head = self.__head
            position = 0
            
            while position < i - 1:
                head = head.get_next()
                position += 1
            if self.__tail != self.__head:
                self.__tail = head
            
            self.__tail.set_next(None)

        else:
            removed_item = self.__head.get_data()
            self.__head = self.__head.get_next()
            if self.__head == None:
                self.__tail = None
        self.__size -= 1

        return removed_item

    
class Node(object):

    # constructor for Node class
    def __init__(self):
        self.__data = None
        self.__prev = None
        self.__next = None
        
    # setters and getters
    def set_next(self, next):
        self.__next = next
    
    def get_next(self):
        return self.__next

    def set_prev(self, prev):
        self.__prev = prev

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class StackParenthesesChecker(object):

    # constructor for StackParenthesesChecker class
    def __init__(self):
        self.__stack = Stack()

    # check if string s has balanced parentheses
    def isBalanced(self, s):
        for char in s:
            if char == "(":
                self.__stack.push(char)
            elif char == ")":
                if self.__stack.isEmpty():
                    return False
                else:
                    self.__stack.pop()
        if self.__stack.isEmpty():
            return True
        self.__stack.clear()
        return False

class QueueParenthesesChecker(object):

    #constructor for QueueParenthesesChecker class
    def __init__(self):
        self.__queue1 = Queue()
        self.__queue2 = Queue()

    # check if string s has balanced parentheses
    def isBalanced(self, s):
        for char in s:
            if char == "(":
                if self.__queue1.isEmpty():
                    self.__queue1.enqueue(char)
                else:
                    while self.__queue1.isEmpty() == False:
                        self.__queue2.enqueue(self.__queue1.dequeue())
                    self.__queue1.enqueue(char)
                    while self.__queue2.isEmpty() == False:
                        self.__queue1.enqueue(self.__queue2.dequeue())
            elif char == ")":
                if self.__queue1.isEmpty():
                    return False
                else:
                    self.__queue1.dequeue()
        if self.__queue1.isEmpty():
            return True
        self.__queue1.clear()
        return False


def main():
    checker1 = StackParenthesesChecker()
    checker2 = QueueParenthesesChecker()
    stack = Stack()
    queue1 = Queue()
    queue2 = Queue()
    setattr(stack, "_Stack__linkedList", LinkedList()) 
    setattr(queue1, "_Queue__linkedList", LinkedList())
    setattr(queue2, "_Queue__linkedList", LinkedList())

    #loop to ask input from user until user wants to stop
    keep_going = "y" 
    while keep_going == "y":
        userString = input("Please enter a string of parentheses: ")
        setattr(checker1, '_Stack__stack', Stack())
        setattr(checker2, '_Queue__queue1', Queue())
        setattr(checker2, '_Queue__queue2', Queue())
        
        if checker1.isBalanced(userString) and checker2.isBalanced(userString): 
            print("The input string {} has balanced parentheses.".format(userString))
   
        else:
            print("The input string {} does not have balanced parentheses.".format(userString))

        keep_going = input("Would you like to continue? (Enter y for yes): ")
        keep_going = keep_going.lower()

    print("Program exited successfully.")

if __name__ == "__main__":
    main()