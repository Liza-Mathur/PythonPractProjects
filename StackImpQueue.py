from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        if not self.q1:
            return "Stack is empty!"
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        popped = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1  # Swap queues
        return popped

    def top(self):
        return self.q1[-1] if self.q1 else "Stack is empty!"

    def is_empty(self):
        return not self.q1

s = StackUsingQueues()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())  # 30
print(s.top())  # 20
