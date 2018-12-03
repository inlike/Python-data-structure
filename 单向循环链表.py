"""如何理解链表：即定义两个对象一个作为节点对象，该节点有两个属性，一个是值，一个是指向下一节点
在定义一个链表，通过函数来实现链表的操作"""


class Node:
    """'节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList():
    """单向循环链表"""
    def __init__(self, node=None):
        self._head = node
        if node:
            node.next = node
            
    def is_empty(self):
        """是否为空"""
        return self._head == None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        cur = self._head
        count = 1
        while cur.next != self._head:
            cur = cur.next
            count += 1
        return count

    def travl(self):
        """遍历整个链表"""
        if self.is_empty():
            return '空链表'
        cur = self._head
        while cur.next != self._head:
            print(cur.elem, end='  ')
            cur = cur.next
        # 特殊情况，最后一个节点
        print(cur.elem)
        print()

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)  # 把值转为节点对象
        if self.is_empty():
            self._head = node
            node.next = node
            return '列表为空, 已添加元素'
        cur = self._head
        while cur.next != self._head:
            cur = cur.next
        node.next = self._head
        self._head = node
        cur.next = node

    def append(self,  item):
        """链表尾部添加元素"""
        node = Node(item)  # 把值转为节点对象
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

    def insert(self,  pos,  item):
        """在指定位置添加元素"""
        node = Node(item)
        if pos < 1:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            per = self._head
            count = 0
            while count < (pos-1):
                count += 1
                per = per.next
            # 循环结后per指向pos-1位置
            node.next = per.next
            per.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():  # 无元素的情况
            return '链表为空'

        cur = self._head
        per = None
        while cur.next != self._head:   # 多元素的情况
            if cur.elem == item:
                # 处理删除节点是头结点的情况

                if cur == self._head:
                    """头节点"""
                    rear = self._head
                    while rear.next == self._head:
                        rear = rear.next
                    self._head = rear.next
                    rear.next = self._head
                else:
                    """中间节点"""
                    per.next = cur.next  # 适用中间元素、尾部元素
                return 
            else:
                per = cur
                cur = cur.next

            """尾节点还考虑只有一个节点的情况"""
        if cur.elem == item:
            if cur == self._head:  # 只有一个节点处理
                # 只有一个节点
                self._head = None
            else:
                per.next = self._head  # 适用中间元素、尾部元素

    def search(self, item):
        """查找节点"""
        if self.is_empty():
            return False
        cur = self._head
        while cur.next != self._head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False


if __name__ == '__main__':

    ll = SingleLinkList()
    ll.add(2)
    ll.travl()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.travl()
    ll.insert(3, 'a')
    ll.travl()
    ll.remove(2)
    ll.remove(6)
    ll.travl()








