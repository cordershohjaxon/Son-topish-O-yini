class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        self.queue.pop(0)

    def __str__(self):
        return f"{self.queue}"

q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(1)
print(q)
q.dequeue()
print(q)