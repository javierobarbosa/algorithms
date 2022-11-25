"""
Time O(1) Space O(N)

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
"""


class MinStackV1:
    def __init__(self):
        self.stack = []
        self.current_min = float('inf')
        self.prev_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.current_min:
            self.prev_min.append(self.current_min)
            self.current_min = val

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.current_min:
                self.current_min = self.prev_min.pop()
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def get_min(self) -> int:
        return int(self.current_min)


class MinStackV2:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append((val, min(val, self.get_min())))
        else:
            self.stack.append(())

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def get_min(self) -> int:
        if self.stack:
            return self.stack[-1][1]

