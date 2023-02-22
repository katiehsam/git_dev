
#!/usr/bin/env python3
"""
atds.py 
Describes the Data Structures used in the Advanced Topics course.
This is the start of Unit 4: Linear Data Structures 
"""

__author__ = "Katie Sam"
__version__ = "2023-01-17"
'''
class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    def __repr__(self):
        return super().__
'''
class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0 

    def size(self):
        return len(self.queue)

    def __repr__(self):
        return "Queue" + str(self.queue)

class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)

    def removeRear(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


def main():
    print("Testing the Stack class") 
    testsPassed = 0
    try:
        s = Stack()
        testsPassed += 1
        print("Test passed: stack created") 
    except:
        print("Test failed: couldn't initialize stack")

    try: 
        s.push("hello")
        s.push(3)
        testsPassed += 1
        print("Test passed: items pushed")
    except:
        print("Test failed: couldn't push onto stack")

    try:
        result = s.peek() 
        if (result == 3):
            testsPassed += 1
            print("Test passed: peeked at item") 
        else:
            print("Test failed: incorrect peek value") 
    except:
        print("Test failed: couldn't peek at stack")

    try:
        result = s.pop()
        if (result == 3):
            testsPassed += 1
            print("Test passed: item popped")
        else:
            print("Test failed: incorrect pop result")
    except:
        print("Test failed: couldn't pop")

    try:
        result = s.is_empty() 
        if (not result):
            testsPassed += 1
            print("Test passed: isEmpty returned correct result") 
        else:
            print("Test failed: stack has items, but indicated empty") 
    except:
        print("Test failed: isEmpty() method unavailable")

    try:
        result = s.size() 
        if (result == 1):
            testsPassed += 1
            print("Test passed: correct size returned")
        else:
            print("Test failed: incorrect size returned") 
    except:
        print("Test failed: .size() method unavailable")

    try: 
        s.pop()
        if s.is_empty():
            testsPassed += 1
            print("Test passed: isEmpty() identified empty stack")
        else:
            print("Test failed: isEmpty() not identified empty stack")
    except: 
        pass
    
    try:
        result = s.is_empty() 
        if (result):
            testsPassed += 1
            print("Test passed: .isEmpty() correctly indicating empty status") 
        else:
            print("Test failed: stack failed to indicate empty status") 
    except:
        print("Test failed: isEmpty() unavailable")
    
    print(str(testsPassed) + "/8 tests passed")

    
if __name__ == "__main__":
    main() 