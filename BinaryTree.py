class Node :
    
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None :
                    self.left = Node(data)
                else :
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else :
                    self.right.insert(data)
        else:
            self.data = data
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def inorderTraversal(self,root):
        res = []
        if root :
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def PreorderTraversal(self,root):
        res = []
        if root :
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def PostorderTraversal(self,root):
        res = []
        if root :
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

    def findval(self,lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None :
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data)+" is Found")


    def Deletion(self, delete) :
        global index

        if delete == self.data and index == 0 :
            self.data = self.right.left.data
            self.right.left.data = ""
        else :
            index = 1

            if delete == self.data and index != 0 : 
                indexleft = 0
                indexright = 0
                if self.left is None and self.right is None :
                    indexleft = 1
                    indexright = 1
                if indexleft == 1 and indexright == 1 :
                    self.data = ""
                else :
                    indexleft = 0
                    indexright = 0
                    if self.left is not None and self.right is not None  :
                        indexleft = 1
                        indexright = 1
                    if indexleft == 1 and indexright == 1 :
                        self.data = self.left.data
                        self.left.data = ""
                    else :
                        if indexleft == 1 and indexright != 1 :
                            self.data = self.left.data
                            self.left.data = ""
                        if indexright == 1 and indexleft != 1 :
                            self.data =  self.right.data
                            self.right.data = ""
            elif delete != self.data  :
                if delete < self.data :
                    return self.left.Deletion(delete)
                elif delete > self.data :
                    return self.right.Deletion(delete)



root = Node(100)
root.insert(50)
root.insert(150)
root.insert(20)
root.insert(60)


root.PrintTree()

print('Inorder Traversal : ',root.inorderTraversal(root))
print('Preorder Traversal : ',root.PreorderTraversal(root))
print('Postorder Traversal : ',root.PostorderTraversal(root))

root.Deletion(60)
print("Deletion Node don't have child : ",root.PostorderTraversal(root))
root.Deletion(50)
print("Deletion Node have child : ",root.PostorderTraversal(root))
root.Deletion(100)
print("Deletion root Node : ",root.PostorderTraversal(root))
