class Stuck:
    def __init__(self):
        self.stuck = []

    def push(self,value):
        self.stuck.append(value)

    def pop_item(self):
        self.stuck.pop()

    def __str__(self):
        return f"{self.stuck}"


stack1 = Stuck()

stack1.push(2)
stack1.push(3)
stack1.push(1)
print(stack1)
stack1.pop_item()
print(stack1)