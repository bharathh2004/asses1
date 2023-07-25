
# 1: Delete the elements in an linked list whose sum is equal to zero
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
 
def getNode(data):
    temp = ListNode(data)
    temp.next = None
    return temp

def printList(head):
    while (head.next):
        print(head.val, end=' -> ')
        head = head.next
    print(head.val, end='')
 
def removeZeroSum(head, K):
    root = ListNode(0)
    root.next = head
    umap = dict()
    umap[0] = root
    sum = 0

    while (head != None):
        sum += head.val
        if ((sum - K) in umap):
 
            prev = umap[sum - K]
            start = prev
            aux = sum
            sum = sum - K
            while (prev != head):
                prev = prev.next
                aux += prev.val
                if (prev != head):
                    umap.remove(aux)
            start.next = head.next
 
    
        else:
            umap[sum] = head
            head = head.next

    return root.next
 
 
if __name__ == '__main__':
    head = getNode(1)
    head.next = getNode(2)
    head.next.next = getNode(-3)
    head.next.next.next = getNode(3)
    head.next.next.next.next = getNode(1)
    K = 5
    head = removeZeroSum(head, K)
    if(head != None):
        printList(head)

# 2:Reverse a linked list in groups of given size
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  
  
class LinkedList:
    def __init__(self):
        self.head = None
  
    def reverse(self, head, k):
        
        if head == None:
          return None
        current = head
        next = None
        prev = None
        count = 0
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        if next is not None:
            head.next = self.reverse(next, k)
        return 
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
  
print("Given linked list")
llist.printList()
llist.head = llist.reverse(llist.head, 3)
  
print ("\nReversed Linked list")
llist.printList()





# 3:Merge a linked list into another linked list at alternate positions

class Node(object):
    def __init__(self, data:int):
        self.data = data
        self.next = None
  
class LinkedList(object):
    def __init__(self):
        self.head = None
          
    def push(self, new_data:int):
        new_node = Node(new_data)
        new_node.next = self.head
  
        self.head = new_node
    
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
              
    def merge(self, p, q):
        p_curr = p.head
        q_curr = q.head
  
        while p_curr != None and q_curr != None:
  
    
            p_next = p_curr.next
            q_next = q_curr.next
            q_curr.next = p_next  
            p_curr.next = q_curr
            p_curr = p_next
            q_curr = q_next
            q.head = q_curr

llist1 = LinkedList()
llist2 = LinkedList()
llist1.push(3)
llist1.push(2)
llist1.push(1)
llist1.push(0)

for i in range(8, 3, -1):
    llist2.push(i)
  
print("First Linked List:")
llist1.printList()
  
print("Second Linked List:")
llist2.printList()
llist1.merge(p=llist1, q=llist2)
  
print("Modified first linked list:")
llist1.printList()
  
print("Modified second linked list:")
llist2.printList()









# 4:In an array, Count Pairs with given sum

def getPairsCount(arr, n, sum):
    unordered_map = {}
    count = 0
    for i in range(n):
        if sum - arr[i] in unordered_map:
            count += unordered_map[sum - arr[i]]
        if arr[i] in unordered_map:
            unordered_map[arr[i]] += 1
        else:
            unordered_map[arr[i]] = 1
    return count
 
arr = [1, 5, 7, -1]
n = len(arr)
sum = 6
print('Count of pairs is', getPairsCount(arr, n, sum))
 










# 5:Find duplicates in an array



arr = [1, 2, 3, 4, 2, 7, 8, 8, 3];     
     print("Duplicate elements in given array: ");      
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            print(arr[j]);






# 6:Find the Kth largest and Kth smallest number in an array
 
def kthSmallest(arr, N, K):
    arr.sort()
    return arr[K-1]
 
if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    N = len(arr)
    K = 2
    print("K'th smallest element is",
          kthSmallest(arr, N, K))



# 7:Move all the negative elements to one side of the array


def move(arr):
  arr.sort()
arr = [ -1, 2, -3, 4, 5, 6, -7, 8, 9 ]
move(arr)
for e in arr:
    print(e , end = " ")


# 8:Reverse a string using a stack data structure


def createStack():
    stack = []
    return stack
 
def size(stack):
    return len(stack)
  
def isEmpty(stack):
    if size(stack) == 0:
        return true
  
def push(stack, item):
    stack.append(item)
 
def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()
 
def reverse(string):
    n = len(string)
    stack = createStack()

    for i in range(0, n, 1):
        push(stack, string[i])
    string = ""
 
    for i in range(0, n, 1):
        string += pop(stack)
    return string
string = "Bharath"
string = reverse(string)
print("Reversed string is " + string)

# 9:Evaluate a postfix expression using stack

class evalpostfix:
    def __init__(self):
        self.stack = []
        self.top = -1
 
    def pop(self):
        if self.top == -1:
            return
        else:
            self.top -= 1
            return self.stack.pop()
 
    def push(self, i):
        self.top += 1
        self.stack.append(i)
 
    def centralfunc(self, ab):
        for i in ab:
            try:
                self.push(int(i))
            except ValueError:
                val1 = self.pop()
                val2 = self.pop()
                if i == '/':
                    self.push(val2 / val1)
                else:
                    switcher = {'+': val2 + val1, '-': val2 -
                                val1, '*': val2 * val1, '^': val2**val1}
                    self.push(switcher.get(i))
        return int(self.pop())
 
if __name__ == '__main__':
    str = '100 200 + 2 / 5 * 7 +'
    strconv = str.split(' ')
    obj = evalpostfix()
    print(obj.centralfunc(strconv))


# 10:Implement a queue using the stack data structure  
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
 
    def enQueue(self, x):
         
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
 
        self.s1.append(x)
 
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def deQueue(self):
        
        if len(self.s1) == 0:
            return -1
        x = self.s1[-1]
        self.s1.pop()
        return x
if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
 
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
























































































































