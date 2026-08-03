class tree:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def insert_the_ele(self, val):
        if self.data:
            if val < self.data:
                if self.left is None:
                    self.left = tree(val)
                else:
                    self.left.insert_the_ele(val)
            elif val > self.data:
                if self.right is None:
                    self.right = tree(val)
                else:
                    self.right.insert_the_ele(val)

    def display(self):
        if self.left:
            self.left.display()
        print(self.data, end=' --> ')
        if self.right:
            self.right.display()

    def pre_order_traversal(self, root):
        if root:
            print(root.data, end=' --> ')
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def in_order_traversal(self, root):
        if root:
            self.pre_order_traversal(root.left)
            print(root.data, end=' --> ')
            self.pre_order_traversal(root.right)

    def post_order_traversal(self, root):
        if root:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.data, end=' --> ')

    def search_ele(self, val):
        if val < self.data:
            if self.left is None:
                print(f"{val} is not found")
                return False
            else:
                self.left.search_ele(val)
        elif val > self.data:
            if self.right is None:
                print(f'{val} is not found')
                return False
            else:
                self.right.search_ele(val)
        else:
            print(f'{val} is found')

    def height(self, root):
        if root is None:
            return 0
        leftHieght = self.left.height(root.left)
        rightHieght = self.right.height(root.right)
        if leftHieght > rightHieght:
            return leftHieght + 1
        return rightHieght + 1




t1 = tree(25)
t1.insert_the_ele(10)
t1.insert_the_ele(25)
t1.insert_the_ele(28)
t1.insert_the_ele(20)
t1.insert_the_ele(7)
t1.insert_the_ele(13)
t1.insert_the_ele(5)
t1.insert_the_ele(9)
t1.display()
print()
t1.search_ele(10)
print()

