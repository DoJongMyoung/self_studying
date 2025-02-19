class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

node1 = TreeNode() #treenode라는 객체 생성
node1.data = 'hs' #node1에는 hs라는 데이터를 갖음

node2 = TreeNode()  # 객체 생성
node2.data = 'sl'
node1.left = node2 #node1.left라는 주소를 node2에 저장

node3 = TreeNode()
node3.data = 'mb'
node1.right = node3

node4 = TreeNode()
node4.data = 'hw'
node2.left = node4

node5 = TreeNode()
node5.data = 'zz'
node2.right = node5

node6 = TreeNode()
node6.data = 'sm'
node3.left = node6

print(node6.data)
print(node1.left.left.data)