class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0

    def prepend(self, data):
        n = Node(data)

        if self.size == 0:
            self.header = n
            self.tail = n
        else:
            n.next = self.header
            self.header = n

        self.size += 1

    def append(self, data):
        n = Node(data)

        if self.size == 0:
            self.header = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

        self.size += 1

    def get(self):
        result = []

        current = self.header
        while current is not None:
            result.append(current.data)
            current = current.next

        return result

    def removeFirst(self):
        if self.size == 0:
            return

        data = self.header.data
        if self.size == 1:
            self.header = None
            self.tail = None
        else:
            self.header = self.header.next

        self.size -= 1
        return data

    def removeLast(self):
        if self.size == 0:
            return

        data = self.tail.data
        if self.size == 1:
            self.header = None
            self.tail = None
        else:
            current = self.header
            while current.next.next is not None:
                current = current.next
            current.next = None
            self.tail = current

        self.size -= 1
        return data

    def insertAt(self, pos, data):
        if pos < 0 or pos > self.size:
            return
        elif pos == 0:
            self.prepend(data)
        elif pos == self.size:
            self.append(data)
        else:
            node = Node(data)

            prev = None
            current = self.header
            count = 0
            while count < pos:
                prev = current
                current = current.next
                count += 1

            node.next = current
            prev.next = node

        self.size += 1
