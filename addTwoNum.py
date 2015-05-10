# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    def addTwoNumbers(self, l1, l2):
        #其实不需要把他们的长度都转换成一样的
        #check length:
        lenl1=0
        checkerl1=l1
        # print "test0"
        while checkerl1:
            lenl1+=1
            checkerl1=checkerl1.next
        lenl2=0
        checkerl2=l2
        # print "test1"
        while checkerl2:
            lenl2+=1
            checkerl2=checkerl2.next
        # print "test2"
        checkerl1=l1
        checkerl2=l2
        while checkerl1.next != None:
            checkerl1=checkerl1.next
        while checkerl2.next != None:
            checkerl2=checkerl2.next
        while lenl1 > lenl2 or lenl1 < lenl2:
            if lenl1 > lenl2:
                # print "aa"
                newNode=ListNode(0)
                checkerl2.next=newNode
                checkerl2=newNode
                lenl2+=1
            else:
                # print "bb"
                newNode=ListNode(0)
                checkerl1.next=newNode
                checkerl1=newNode
                lenl1+=1
        # cnode=l2
        # while cnode !=None:
        #     print cnode.val
        #     cnode=cnode.next
        currentVal = l1.val + l2.val
        count=0
        if currentVal < 10:
            rootNode = ListNode(currentVal)
        else:
            currentVal=currentVal - 10
            rootNode = ListNode(currentVal)
            count=1
        preNode=rootNode
        l1=l1.next
        l2=l2.next
        while l1 != None and l2 != None or count!=0:
            currentVal=0
            # print str(l1.val)+" "+str(l2.val)+" "+str(count)
            if l1 != None and l2 != None:
                currentVal += l1.val + l2.val
                l1=l1.next
                l2=l2.next
            if count != 0:
                currentVal += count
            if currentVal < 10:
                # print "aaa: "+str(currentVal)
                currentNode = ListNode(currentVal)
                count=0
            else:
                currentVal=currentVal - 10
                currentNode = ListNode(currentVal)
                count=1
            preNode.next=currentNode
            preNode = currentNode
        # return rootNode
        # print:
        cnode=rootNode
        while cnode !=None:
            print cnode.val
            cnode=cnode.next

if __name__ == '__main__':
    first=ListNode(1)
    second=ListNode(8)
    third=ListNode(3)
    first.next=second
    second.next=third
    fourth=ListNode(7)
    fifth=ListNode(1)
    fourth.next=fifth
    Solution().addTwoNumbers(first, fourth)