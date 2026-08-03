class node:
    def __init__(self, data):
        self.data=data
        self.addr=None
class Single_Linked_List:
    def __init__(self):
        self.head=None

    def insert_at_last(self,val):
        newNode=node(val)
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            while temp.addr!=None:
                temp=self.addr
            temp.addr=newNode

    def diplay(self):
        if self.head is None:
            print("No node to display")
        else:
            temp=self.head
            while temp:
                print(temp.data, end='-->')
                temp=temp.addr
            print()
    
    def length(self):
        if self.head is None:
            print("NO node to count")
        else:
            temp=self.head
            cnt=0
            while temp:
                cnt+=1
                temp=temp.addr
            return cnt
    
    def insert_at_first(self,val):
        newNode=node(val)
        if self.head is None:
            self.head=newNode
        else:
            newNode.addr=self.head
            self.head=newNode
    
    def insert_at_loc(self, val, loc):
        newNode=node(val)
        if loc<=0:
            print("Enter loc above 0")
        elif loc==1:
            self.insert_at_first(val)
        elif loc == self.length()+1:
            self.insert_at_last(val)
        elif loc> self.length():
            print("Enter the loc less than :", self.length())
        else:
            temp=self.head
            cnt=1
            while temp.addr!=None and cnt<loc-1:
                temp=temp.addr
                cnt+=1
            newNode.addr=temp.addr
            temp.addr=newNode
    
    def delete_at_last(self):
        if self.head is None:
            print("No node to delete")
        elif self.length()==1:
            self.head=None
        else:
            temp=self.head
            while temp.addr.addr!=None:
                temp=temp.addr
            temp.addr=None
    
    def delete_at_first(self):
        if self.head is None:
            print("No nodes to delete")
        elif self.length==1:
            self.head=None
        else:
            self.head=self.head.addr

    def delete_at_loc(self, loc):
        if loc<=0:
            print("Enter loc above 0")
        elif loc==1:
            self.delete_at_first()
        elif loc==self.length():
            self.delete_at_last()
        elif loc > self.length():
            print("Enter the location less than :",self.length())
        else:
            temp=self.head
            cnt=1
            while temp.addr!=None and cnt<loc-1:
                temp=temp.addr
                cnt+=1
            temp.addr=temp.addr.addr

s1=Single_Linked_List()
while True:
    print("-------- Single Linked List Operations ---------")
    print("1. insert_at_last\n2. Display\n3. Length\n4. insert_at_first\n5. insert_at_loc\n6. delete_at_last\n7. delete_at_first\n8. detele_at_loc\n9. Exit\n ")
    opt=int(input("Enter the option\n"))
    match opt:
        case 1:
            val=input("Enter the value :")
            s1.insert_at_last(val)
        case 2:
            s1.diplay()
        case 3:
            s1.length()
        case 4:
            val=input("Enter the value :")
            s1.insert_at_first(val)
        case 5:
            val=input("Enter the val :")
            loc=int(input("Enter the location :"))
            s1.insert_at_loc(val, loc)
        case 6:
            s1.delete_at_last()
        case 7:
            s1.delete_at_first()
        case 8:
            loc=int(input("Enter the location :"))
            s1.delete_at_loc(loc)
        case _:
            exit()
