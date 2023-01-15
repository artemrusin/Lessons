class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def isPalindrome(self,head):
    x=[head.val]
    buff=head
    while buff.next!=None:
            buff=buff.next
            x+=[buff.val]

    ans=True
    for i in range((len(x)+1)//2):
        print(x[i])
        print(x[-i-1])
        if x[i]!=x[-i-1]:
            return False
    return True

def print_listnode(head):
        print(head.val, end=' ')
        if head.next!=None:
                print_listnode(head.next)

def make_list(head):
        x=[head.val]
        buff=head
        while buff.next!=None:
                buff=buff.next
                x+=[buff.val]
        return x

def make_list_test(head):
        x=[head.val]
        while head.next!=None:
                head=head.next
                x+=[head.val]
        return x


isPalindrome([1,2,3,4,5])
head=ListNode(5)
buff=ListNode(2, head)
head=buffч
buff=ListNode(4, head)
head=buff


