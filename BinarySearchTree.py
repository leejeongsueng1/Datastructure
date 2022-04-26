class Node:
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
    
    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal
    
    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self

    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self

    def lookup(self,key,parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key,self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key,self)
            else:
                return None, None
        else:
            return self, parent

    def insert(self,key,data):
        if key < self.key:
            if self.left:
                self.left.insert(key,data)
            else:
                self.left = Node(key,data)
        elif key > self.key:
            if self.right:
                self.right.insert(key,data)
            else:
                self.right = Node(key,data)
        else:
            raise KeyError('Inserted key is already exist')



class BinSearchTree:
    def __init__(self):
        self.root = None
    
    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []
    
    def min(self):
        if self.root:
            return self.root.min()

        else: 
            return None

    def max(self):
        if self.root:
            return self.root.max()
        else:
            return None

    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None

    def insert(self,key,data):
        if self.root:
            self.root.insert(key,data)
        else:
            self.root = Node(key,data)
    
    # 자식노드의 개수를 파악하는 메소드
    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count


    # 삭제
    # 해당 키에 해당하는 노드를 삭제하고도 이진탐색트리의 성질을 유지하도록 해야함
    # 삭제되는 노드가
    #   1. 말단(leaf) 노드인 경우
            # 그냥 그 노드를 없애면 됨
            # 부모 노드의 링크를 조정 (좌, 우)
    #   2. 자식을 하나 가지고 있는 경우
            # 삭제되는 노드 자리에 그 자식을 대신 배치          
    #   3. 자식을 둘 가지고 있는 경우
            # 삭제되는 노드보다 바로 다음 (큰) 키를 가지는 노드를 찾아
            # 그 노드를 삭제되는 노드 자리에 대신 배치하고
            # 이 노드를 대신 삭제
    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            # The simplest case of no children
            if nChildren == 0:
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # parent.left 또는 parent.right 를 None 으로 하여
                # leaf node 였던 자식을 트리에서 끊어내어 없앱니다.
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 를 None 으로 하여 빈 트리로 만듭니다.
                else:
                    self.root = None
            # When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                # 그 자식을 어떤 변수가 가리키도록 합니다.
                if node.left:
                    tmp = node.left
                else:
                    tmp = node.right
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node 의 자리에 넣습니다.
                if parent:
                    if parent.left == node:
                        parent.left = tmp
                    else:
                        parent.right = tmp
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 에 위에서 가리킨 자식을 대신 넣습니다.
                else:
                    self.root = tmp
            # When the node has both left and right children
            else:
                parent = node
                successor = node.right
                # parent 는 node 를 가리키고 있고,
                # successor 는 node 의 오른쪽 자식을 가리키고 있으므로
                # successor 로부터 왼쪽 자식의 링크를 반복하여 따라감으로써
                # 순환문이 종료할 때 successor 는 바로 다음 키를 가진 노드를,
                # 그리고 parent 는 그 노드의 부모 노드를 가리키도록 찾아냅니다.
                while successor.left:
                    parent = successor
                    successor = successor.left
                # 삭제하려는 노드인 node 에 successor 의 key 와 data 를 대입합니다.
                node.key = successor.key
                node.data = successor.data
                # 이제, successor 가 parent 의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                # 그에 따라 parent.left 또는 parent.right 를
                # successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 합니다.
                if parent.right == successor:
                    if successor.right:
                        parent.right = successor.right
                    else:
                        parent.right = None
                else:
                    if successor.right:
                        parent.left = successor.right
                    else:
                        parent.left = None

            return True

        else:
            return False


    