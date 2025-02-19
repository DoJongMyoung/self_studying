class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    node = TreeNode()
    node.data = numbers[0]
    root = node #루트는 주소를 의미

    for group in numbers[1:]: #그룹의 index=1번쨰 요소부터 for문 시작
        node = TreeNode()
        node.data = group #group에 해당하는 값을 node.data에 할당
        current = root # 최신 주소
        while True:
            if group < current.data: #그룹의 요소가 current에 들어있는 데이터보다 작으면
                if current.left is None:
                    current.left = node # 왼쪽이 없으면 할당
                    break
                current = current.left  # move 왼쪽으로 이동
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right  # move

    print("BST 구성 완료")

    find_group = int(input())

    current = root
    while True:
        if find_group == current.data:
            print(f"{find_group}을(를) 찾았습니다")
            break
        elif find_group < current.data:
            if current.left is None:
                print(f"{find_group}이(가) 존재하지 않습니다")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{find_group}이(가) 존재하지 않습니다")
                break
            current = current.right