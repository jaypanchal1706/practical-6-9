"""
    Name = Panchal Jay Manojkumar
    Id = 20CE068


    Github Link = https://github.com/jaypanchal1706/practical-6-7.git

"""
# class Stack is defined
class Stack(object):

    def __init__(self):
        self.item = []
    # push function add the item in the list
    def push(self, item = ''):

        self.item.append(item)
        pass
    # pop function pop the item from the list
    def pop(self):

        self.item.pop()
        pass
    # peek function to use return top element of the stack
    def peek(self):

        if self.item:
            return self.item[-1]
        else:
            return None
    # size function returns size of the stack
    def size(self):
        if self.item:
            return len(self.item)
        else:
            return None

    def isempty(self):

        if self.item == []:
            return True
        else:
            return False

if __name__ == "__main__":
    stack = Stack()

    stack.push("1")
    stack.push('2')
    print(stack.size())
    print(stack.peek())

    stack.pop()
    print(stack.size())
    print(stack.peek())

    print(stack.isempty())
    print(stack.pop())
    stack.push("4")
    print(stack.peek())








