class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

class SLinkedList:
   def __init__(self):
      self.head = None

   def listprint(self):
      val = self.head
      while val is not None:
         print (val.data)
         val = val.next

   def countNodes(self):
        count = 0
        val = self.head
        while val:
            val = val.next
            count += 1
        return count
   
   def findMiddle(self):
        slow, fast = self.head,self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
   def findKNodesFrmLst(self, k):
        pass



            

    









list = SLinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thu")
e5 = Node("Fri")
e6 = Node("Sat")
e7 = Node("Sun")


list.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = e7


        
        


    


    






