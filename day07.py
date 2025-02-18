#큐

class Node:
    def __init__(self, data, next=None): #data를 보관할 data변수 // 다음노드의 주소를 찍을 next변수 , 따로 설정하지 않으면 None
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, data):
        self._size = self._size + 1
        node = Node(data)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node #주소 설정
            self.rear = node # 값 설정

    def dequeue(self):
        if self.front is None:
            raise IndexError("빈 큐입니다")
        self._size = self._size - 1
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data