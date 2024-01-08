class Stack:
    def __init__(self):
        self.__object = []
    
    def push(self, elements):
        self.__object.append(elements)
    
    def is_empty(self):
        if len(self.__object) == 0:
            return True
    
    def pop(self):
        if self.is_empty():
            return "Sorry the stack is empty"
        else:
            self.pop()
        
    def peek(self):
        if self.is_empty():
            return print("Sorry the stack is empty")
        else:
            print(self.__object[0])


def main():
    stack = Stack()
    stack.peek()
    stack.push("Ezreal")
    stack.push("Jhin")
    stack.peek()


main()