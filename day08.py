def pre_order(node):
    if node is None: #노드가 비어있으면
        return
    print(node.data, end='-') # 현1-2-4-5 왼 3-6오
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end='-') # 왼4-2-5 -1현 -6-3오
    in_order(node.right)


def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end='-') #    왼쪽(4 - 5 - 2) - 오른쪽(6 - 3)- 1


class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

node1 = TreeNode()
node1.data = 'hs1'

node2 = TreeNode()
node2.data = 'sl2'
node1.left = node2

node3 = TreeNode()
node3.data = 'mb3'
node1.right = node3

node4 = TreeNode()
node4.data = 'hw4'
node2.left = node4

node5 = TreeNode()
node5.data = 'zz5'
node2.right = node5

node6 = TreeNode()
node6.data = 'sm6'
node3.left = node6


# post_order(node1)
# print()
pre_order(node1)
# print()
# in_order(node1)