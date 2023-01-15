class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def len_listnode(head):
    lenln=1
    while head.next!=None:
        lenln+=1
        head=head.next
    return lenln

def add_listnode(head,buff):
    if head==None:
        return buff
    else:
        buff2=head
        while buff2.next!=None:
            buff2=buff2.next
        buff2.next=buff
        
        return head



def print_listnode(head):
        print(head.val, end=' ')
        if head.next!=None:
                print_listnode(head.next)

        print()

head1=ListNode(4)
buff=ListNode(2, head1)
head1=buff
buff=ListNode(1, head1)
head1=buff

head2=ListNode(4)
buff=ListNode(3, head2)
head2=buff
buff1=ListNode(1, head2)
head2=buff1

head3=None




print_listnode(head1)
print_listnode(head2)

while head1!=None and head2!=None:
    if head1.val<head2.val:
        buff=head1
        head1=head1.next
    else:
        buff=head2
        head2=head2.next
    buff.next=None
    if head3==None:
        head3=buff
    else:
        last.next=buff
    last=buff
    print_listnode(head3)
            


if head1==None:
        head1=head2

print_listnode(head3)

head3=add_listnode(head3,head1)

print_listnode(head3)
