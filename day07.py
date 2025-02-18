#링크드 리스트
#데이터를 담는 부분과 노트를 가르키는 부분으로 이루어져 있음.

class Node:
    def __init__(self, data, next=None): #data를 보관할 data변수 // 다음노드의 주소를 찍을 next변수 , 따로 설정하지 않으면 None
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if not self.head: # self.head가 None일시 실행
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def search(self, target):
        current = self.head
        while current.next:
            if current.data == target:
                return True
            else:
                current = current.next
        return False