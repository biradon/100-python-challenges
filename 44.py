
class Stack:
    def __init__(self):
        self.__values = []
    def push(self,elements):
        self.__values.append(elements)
    
    def pop(self):
        return self.__values.pop()
    
    def is_empty(self):
        return len(self.__values) == 0
    
    def check(self):
        print(self.__values)



def reverse(values):
    result = []
    for i in range(len(values)-1,-1,-1):
        result.append(values[i])
    return result

def reverse_update(values):
    left = 0
    right = len(values) - 1
    while left < right:
        temp = values[left]
        values[left] = values[right]
        values[right] = temp
        left += 1
        right -= 1
    return values

def reverse_using_stack(values):
    stack = Stack()
    for elements in values:
        stack.push(elements)
    stack.check()
    result = []
    while not stack.is_empty():
        result.append(stack.pop())
    stack.check()
    return result

# print(reverse([1,2,3,4]))
# print(reverse(["A","BB","CCC","DDDD"]))
# print(reverse_update([1,2,3,4]))
# print(reverse_update(["A","BB","CCC","DDDD"]))
print(reverse_using_stack([1,2,3,4]))
print(reverse_using_stack(["A","BB","CCC","DDDD"]))